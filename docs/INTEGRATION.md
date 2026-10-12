# 数据维护与既有任务接入

`data/papers.json` 是唯一论文数据源。`README.md` 与 `dist/index.html` 是确定性生成结果，不要手改。阅读器内嵌样式、脚本与论文内容，可直接离线打开。

本仓库没有创建新定时任务，也没有安装 GitHub Actions 计划。既有任务仍需通过支持的任务管理入口接入；在未取得真实任务 ID、完整原提示词、时区和执行环境前，不应宣称每日同步已经生效。

## 本地使用

要求 Python 3.9+；阅读器测试要求 Node 18+。所有脚本无第三方依赖。推送还需要已有登录的 GitHub CLI 与 Git。

```bash
python3 scripts/paper_watch.py validate
python3 scripts/paper_watch.py build
python3 scripts/paper_watch.py build --check
python3 -m unittest discover -s tests -v
node --test tests/reader.test.cjs
```

直接用浏览器打开 `dist/index.html`。E 全部展开，C 全部收起；搜索框、选择框、可编辑内容、输入法组合期间和任何修饰键组合均不触发快捷键。可关闭快捷键，所有操作均有可聚焦按钮。筛选不改变展开状态；全部展开/收起包括当前被筛选隐藏的论文。

GitHub README 使用每篇 `<details>` 折叠；批量快捷键由 HTML 阅读器提供。本项目没有自动启用 Pages。

## 增量数据格式

批次是一个 UTF-8 JSON 对象：`{"schema_version":1,"papers":[...]}`。空数组是合法的“本次无新增”。仅导出经过核实的公开论文资料，原始批次放在被 Git 忽略的 `incoming/`。

每篇字段如下。未知值使用 `null`，不能猜测。

| 字段 | 含义 |
| --- | --- |
| `title`, `short_name` | 论文完整标题、简短名称，单行纯文本 |
| `published` | 首次公开日期 `YYYY-MM-DD`；未知为 `null`，不能用收录日期替代 |
| `category` | 视频生成基础 / 少步蒸馏 / 交互长视频 / 流式系统 / 具身与世界模型 / 交互 Avatar |
| `tags` | 最多 12 个短标签组成的数组 |
| `arxiv_id` | 如 `2412.07772`；无则 `null`，版本号会被去除 |
| `doi` | 已核实 DOI；无则 `null` |
| `paper_url` | 可公开访问的论文详情链接，优先 arXiv 或 DOI |
| `links` | `project`、`code`、`weights` 三个键；已验证官方链接或 `null` |
| `summary` | `problem`、`method`、`value`、`limitation` 四个键，合计 80–160 字符的独立中文提炼 |
| `evidence_urls` | 至少一个作者论文、官方项目或官方仓库等一手来源 URL |
| `verified_at` | 本次实际核验日期 `YYYY-MM-DD` |
| `id` | 可省略，由导入器根据标识生成 |
| `first_seen`, `last_seen`, `discovery_sources` | 批次可省略，由导入命令记录；不要填私人任务 ID |

数据示例见 `data/papers.json` 中的真实条目。脚本拒绝未知字段、文件路径、私网链接、带凭据的 URL、明显凭据字符串、HTML 和多行原始笔记。这些格式约束不能代替对公开范围和论文真实性的核验。

## 三个来源共同导入

三个来源标记是 `video-avatar`、`embodied-world`、`interactive-video`；初始精选为 `vigen-seed`。这些标记不是调度器 ID，不创建任务。

```bash
# 仅核验和预览合并统计，不写论文文件、不联网
python3 scripts/paper_watch.py import incoming/2026-10-12-interactive-video.json --source interactive-video --date 2026-10-12 --dry-run

# 本地合并并重新生成两个展示文件，不提交、不推送
python3 scripts/paper_watch.py import incoming/2026-10-12-interactive-video.json --source interactive-video --date 2026-10-12
```

去重比较所有可用身份：去版本 arXiv ID、大小写归一 DOI、规范论文 URL。arXiv DOI 与对应 arXiv ID 互通。URL 去除 fragment、常见跟踪参数和末尾斜杠，保留真正的查询参数；不因标题相似而合并。

重复执行同日批次是幂等的；不同来源命中同一论文合并来源集合。较新核验内容更新旧摘要；未知链接不删除已验证链接。冲突的论文标识会停止导入。`flock` 串行化本机并发运行，文件分别原子替换；如进程在多文件写入间意外中断，可重新执行 `build` 修复展示结果。同一仓库应使用同一个本地 checkout；多个主机同时推送仍可能产生 Git 分歧，需人工合并。

## 已授权任务的自动推送命令

从干净的仓库开始，直接让发布脚本完成“拉取 → 导入 → 生成 → 测试 → 提交 → 推送 → 核对远程提交”；不要先运行会修改工作树的本地导入。

```bash
# 默认只预览，不写论文文件、不联网
python3 scripts/publish.py incoming/2026-10-12-interactive-video.json --source interactive-video --date 2026-10-12

# 仅在本批次已经过公开内容核验后执行
python3 scripts/publish.py incoming/2026-10-12-interactive-video.json --source interactive-video --date 2026-10-12 --push
```

发布目标固定为 `RipeMangoBox/research-paper-watch`，要求 `main` 分支、干净工作树、已有 `RipeMangoBox` 登录。只暂存 `data/papers.json`、`README.md`、`dist/index.html`；已有未推送提交也必须只涉及这三个文件。不创建 token，不上传输入批次或其他文件，不强制推送、不改 GitHub 权限。

失败会停止并保留本地状态；若仅推送失败且工作树仍干净，可重试相同命令。权限错误、脏工作树或分歧不得通过覆盖或强制推送解决。

## 拟追加到既有任务末尾的指令

将下面指令中的来源标记替换为对应值，保留原任务的时间、时区、监控条件、研究范围和主体提示词。只在已核实任务确实能使用该本地 checkout、Python、Node、Git 和现有 GitHub 登录时接入。

> 完成原有研究后，将本次实际核实、符合原研究范围的公开论文整理为本仓库约定的 JSON 增量批次，保存到 `incoming/日期-来源标记.json`。每篇只含公开标题、身份标识、公开日期、官方论文/项目/代码/权重链接、分类和 80–160 字中文简介，涵盖问题、方法、价值与局限，并记录一手证据 URL 与实际核验日期。没有核实的链接填 null，不包含 PDF、私人笔记、内部实验、原始对话或研究私密计划。使用对应来源标记运行 `scripts/publish.py` 先预览，然后以 `--push` 完成已授权的公开仓库同步；核对返回的远程提交哈希后再报告成功。本次无符合条件的新论文时使用空批次，不编造新增。遇到访问、验证或推送失败时保留批次并明确报告未同步，不新建任务、不改原时间、不扩权、不强制推送。

若任务运行在无法执行本地脚本的网页 ChatGPT 环境，不能仅追加此指令就视为已接通。需要支持的 GitHub 写入/执行桥接或可访问的本地执行器，并进行一次真实任务输出的端到端验证。不要新建重复日程来掩盖原任务未接入。

## 首批数据核验

七篇均重新核对公开论文页及官方仓库，链接证据和日期保存在各条目中。Diffusion Forcing 没有添加未独立验证的权重入口。LongLive 对应原始一代论文，Causal Forcing 对应原始三阶段方法。中文简介没有复制本地私人长篇解析，未上传本地 PDF 或源码副本。

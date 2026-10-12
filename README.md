# Research Paper Watch

公开论文精选：视频生成、交互 Avatar、具身与世界模型。每篇附可折叠中文简介与一手来源。

**7 篇论文** · [下载离线阅读器](https://raw.githubusercontent.com/RipeMangoBox/research-paper-watch/main/dist/index.html) · [唯一数据源](data/papers.json) · [导入与任务接入](docs/INTEGRATION.md)

阅读器下载后用浏览器打开：支持搜索、分类、E 全部展开、C 全部收起，也可使用按钮。GitHub README 使用每篇原生折叠块；批量快捷键在阅读器中提供。

日期为论文首次公开日期；空链接表示尚未核实。简介中的局限包含基于公开证据的阅读边界，不代表作者自述的缺陷。

## 目录

- [视频生成基础](#视频生成基础) · 1
- [少步蒸馏](#少步蒸馏) · 3
- [交互长视频](#交互长视频) · 2
- [流式系统](#流式系统) · 1

## 视频生成基础

### Diffusion Forcing

**Diffusion Forcing: Next-token Prediction Meets Full-Sequence Diffusion**<br>
2024-07-01 · 序列建模 / 独立噪声 / 规划<br>
<a href="https://arxiv.org/abs/2407.01392" rel="noopener noreferrer">Paper</a> · <a href="https://www.boyuan.space/diffusion-forcing" rel="noopener noreferrer">Project</a> · <a href="https://github.com/buoyancy99/diffusion-forcing" rel="noopener noreferrer">Code</a>

<details>
<summary>中文简介：问题 · 方法 · 价值 · 局限</summary>

- **问题**：序列预测的灵活长度与整段扩散的引导能力难以兼得。
- **方法**：训练时为各个序列元素独立设置噪声等级，以因果模型学习不同噪声组合下的去噪。
- **价值**：统一变长生成、长时序外推和规划引导，为视频及决策提供通用思路。
- **局限**：原论文使用循环网络；当前主分支已改为时序注意力，复现需区分版本。

来源：<a href="https://arxiv.org/abs/2407.01392">[1]</a> · <a href="https://github.com/buoyancy99/diffusion-forcing">[2]</a> · <a href="https://www.boyuan.space/diffusion-forcing">[3]</a>
核验：2026-10-12

</details>


## 少步蒸馏

### Causal Forcing

**Causal Forcing: Autoregressive Diffusion Distillation Done Right for High-Quality Real-Time Interactive Video Generation**<br>
2026-02-02 · ODE 初始化 / 交互视频 / 因果教师<br>
<a href="https://arxiv.org/abs/2602.02214" rel="noopener noreferrer">Paper</a> · <a href="https://thu-ml.github.io/CausalForcing.github.io" rel="noopener noreferrer">Project</a> · <a href="https://github.com/thu-ml/Causal-Forcing" rel="noopener noreferrer">Code</a> · <a href="https://huggingface.co/zhuhz22/Causal-Forcing/tree/main" rel="noopener noreferrer">Weights</a>

<details>
<summary>中文简介：问题 · 方法 · 价值 · 局限</summary>

- **问题**：双向教师的轨迹初始化与因果学生存在结构不匹配。
- **方法**：先训练自回归教师，再用因果常微分方程轨迹初始化少步学生，随后进行非对称分布匹配蒸馏。
- **价值**：改善蒸馏起点，在既定实验设置中提高视频质量与运动表现。
- **局限**：本条针对原始三阶段方法；后续增强版另有一致性蒸馏，不能混用其结论。

来源：<a href="https://arxiv.org/abs/2602.02214">[1]</a> · <a href="https://github.com/thu-ml/Causal-Forcing">[2]</a> · <a href="https://huggingface.co/zhuhz22/Causal-Forcing/tree/main">[3]</a> · <a href="https://thu-ml.github.io/CausalForcing.github.io">[4]</a>
核验：2026-10-12

</details>

### Self Forcing

**Self Forcing: Bridging the Train-Test Gap in Autoregressive Video Diffusion**<br>
2025-06-09 · 分布匹配 / 自生成历史 / 训练推理对齐<br>
<a href="https://arxiv.org/abs/2506.08009" rel="noopener noreferrer">Paper</a> · <a href="https://self-forcing.github.io/" rel="noopener noreferrer">Project</a> · <a href="https://github.com/guandeh17/Self-Forcing" rel="noopener noreferrer">Code</a> · <a href="https://huggingface.co/gdhe17/Self-Forcing/tree/main" rel="noopener noreferrer">Weights</a>

<details>
<summary>中文简介：问题 · 方法 · 价值 · 局限</summary>

- **问题**：真实历史训练与模型生成历史推理之间的偏差会累积。
- **方法**：训练中直接自回归展开并缓存自生成历史，用整段视频损失监督，配合少步去噪与随机梯度截断。
- **价值**：将训练条件贴近部署过程，支持低延迟流式视频生成。
- **局限**：演示依赖指定硬件与模型设置；长而详细的提示词效果更好，不能外推所有场景。

来源：<a href="https://arxiv.org/abs/2506.08009">[1]</a> · <a href="https://github.com/guandeh17/Self-Forcing">[2]</a> · <a href="https://huggingface.co/gdhe17/Self-Forcing/tree/main">[3]</a> · <a href="https://self-forcing.github.io/">[4]</a>
核验：2026-10-12

</details>

### CausVid

**From Slow Bidirectional to Fast Autoregressive Video Diffusion Models**<br>
2024-12-10 · DMD / KV cache / 自回归<br>
<a href="https://arxiv.org/abs/2412.07772" rel="noopener noreferrer">Paper</a> · <a href="https://causvid.github.io/" rel="noopener noreferrer">Project</a> · <a href="https://github.com/tianweiy/CausVid" rel="noopener noreferrer">Code</a> · <a href="https://huggingface.co/tianweiy/CausVid/tree/main/autoregressive_checkpoint" rel="noopener noreferrer">Weights</a>

<details>
<summary>中文简介：问题 · 方法 · 价值 · 局限</summary>

- **问题**：双向视频扩散依赖未来帧，难以低延迟逐帧生成。
- **方法**：通过教师轨迹初始化、非对称分布匹配蒸馏及因果注意力，将多步模型转为少步自回归生成器。
- **价值**：结合缓存支持流式生成，并展示动态提示与长视频能力。
- **局限**：少步生成仍依赖教师质量；公开仓库的示例训练不等同于论文全部实验。

来源：<a href="https://arxiv.org/abs/2412.07772">[1]</a> · <a href="https://causvid.github.io/">[2]</a> · <a href="https://github.com/tianweiy/CausVid">[3]</a> · <a href="https://huggingface.co/tianweiy/CausVid/tree/main/autoregressive_checkpoint">[4]</a>
核验：2026-10-12

</details>


## 交互长视频

### Rolling Forcing

**Rolling Forcing: Autoregressive Long Video Diffusion in Real Time**<br>
2025-09-29 · 注意力锚点 / 滚动窗口 / 长视频<br>
<a href="https://arxiv.org/abs/2509.25161" rel="noopener noreferrer">Paper</a> · <a href="https://kunhao-liu.github.io/Rolling_Forcing_Webpage" rel="noopener noreferrer">Project</a> · <a href="https://github.com/TencentARC/RollingForcing" rel="noopener noreferrer">Code</a> · <a href="https://huggingface.co/TencentARC/RollingForcing" rel="noopener noreferrer">Weights</a>

<details>
<summary>中文简介：问题 · 方法 · 价值 · 局限</summary>

- **问题**：逐帧生成的误差容易在长视频中持续传播。
- **方法**：在滚动窗口内联合去噪不同噪声等级的帧，保留初始帧缓存作全局锚点，并以非重叠窗口训练。
- **价值**：在控制训练成本的同时改善长时一致性，展示分钟级实时流式视频。
- **局限**：联合窗口放宽了相邻帧严格因果性；长视频展示不等于对任意时长的稳定保证。

来源：<a href="https://arxiv.org/abs/2509.25161">[1]</a> · <a href="https://github.com/TencentARC/RollingForcing">[2]</a> · <a href="https://huggingface.co/TencentARC/RollingForcing">[3]</a> · <a href="https://kunhao-liu.github.io/Rolling_Forcing_Webpage">[4]</a>
核验：2026-10-12

</details>

### LongLive

**LongLive: Real-time Interactive Long Video Generation**<br>
2025-09-26 · KV recache / 提示词切换 / 长时训练<br>
<a href="https://arxiv.org/abs/2509.22622" rel="noopener noreferrer">Paper</a> · <a href="https://nvlabs.github.io/LongLive" rel="noopener noreferrer">Project</a> · <a href="https://github.com/NVlabs/LongLive" rel="noopener noreferrer">Code</a> · <a href="https://huggingface.co/Efficient-Large-Model/LongLive-1.3B" rel="noopener noreferrer">Weights</a>

<details>
<summary>中文简介：问题 · 方法 · 价值 · 局限</summary>

- **问题**：长视频既要保持一致性，也要及时响应用户提示变化。
- **方法**：用提示切换时的缓存重算、流式长时训练，以及短窗口注意力和帧锚点维持生成状态。
- **价值**：将短片模型扩展到可交互的分钟级生成，兼顾响应速度与持续叙事。
- **局限**：本条对应原始一代论文；速度与时长取决于硬件和配置，不代表任意设备表现。

来源：<a href="https://arxiv.org/abs/2509.22622">[1]</a> · <a href="https://github.com/NVlabs/LongLive">[2]</a> · <a href="https://huggingface.co/Efficient-Large-Model/LongLive-1.3B">[3]</a> · <a href="https://nvlabs.github.io/LongLive">[4]</a>
核验：2026-10-12

</details>


## 流式系统

### StreamDiffusionV2

**StreamDiffusionV2: A Streaming System for Dynamic and Interactive Video Generation**<br>
2025-11-10 · 多 GPU / 实时视频 / 系统调度<br>
<a href="https://arxiv.org/abs/2511.07399" rel="noopener noreferrer">Paper</a> · <a href="https://streamdiffusionv2.github.io/" rel="noopener noreferrer">Project</a> · <a href="https://github.com/chenfengxu714/StreamDiffusionV2" rel="noopener noreferrer">Code</a> · <a href="https://huggingface.co/jerryfeng/StreamDiffusionV2" rel="noopener noreferrer">Weights</a>

<details>
<summary>中文简介：问题 · 方法 · 价值 · 局限</summary>

- **问题**：离线吞吐优化难以满足直播首帧延迟与逐帧截止时间。
- **方法**：通过延迟目标感知调度、滚动缓存与跨去噪步骤和网络层的流水线组织视频扩散推理。
- **价值**：无需额外训练即可支持交互视频流和多卡扩展，连接模型与实时服务。
- **局限**：高帧率报告有特定多卡条件；系统加速不等于底层模型生成能力提升。

来源：<a href="https://arxiv.org/abs/2511.07399">[1]</a> · <a href="https://github.com/chenfengxu714/StreamDiffusionV2">[2]</a> · <a href="https://huggingface.co/jerryfeng/StreamDiffusionV2">[3]</a> · <a href="https://streamdiffusionv2.github.io/">[4]</a>
核验：2026-10-12

</details>

## 维护

Python 3.9+，无第三方依赖。

```bash
python3 scripts/paper_watch.py validate
python3 scripts/paper_watch.py build --check
python3 -m unittest discover -s tests -v
node --test tests/reader.test.cjs
```

数据和源码公开；不收录 PDF、私人笔记、实验记录或会话原文。三个既有任务的自动接入仍需核实任务 ID 与执行能力，仓库本身不创建新定时任务。

组织形式参考 [Awesome-Video-Diffusion](https://github.com/showlab/Awesome-Video-Diffusion)。摘要为本项目独立撰写；论文、模型和源码的使用条件以各原始发布方为准。

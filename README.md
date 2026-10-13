# Research Paper Watch

公开论文精选：视频、三维与具身、智能体、多模态检索、评测及训练推理。每篇附可折叠中文简介与一手来源。

**50 篇论文** · [在线阅读（支持快捷键）](https://ripemangobox.github.io/research-paper-watch/) · [下载离线阅读器 ZIP](https://ripemangobox.github.io/research-paper-watch/research-paper-watch.zip) · [唯一数据源](data/papers.json) · [导入与任务接入](docs/INTEGRATION.md)

在线阅读页直接支持搜索、分类、E 全部展开、C 全部收起。离线 ZIP 解压后双击 index.html，无需安装或启动服务器。GitHub README 不运行自定义脚本：可点击简介，或 Tab 聚焦后按 Enter / 空格展开收起；E / C 请使用在线阅读页。

日期为论文首次公开日期；空链接表示尚未核实。简介中的局限包含基于公开证据的阅读边界，不代表作者自述的缺陷。

## 目录

- [视频生成基础](#视频生成基础) · 3
- [少步蒸馏](#少步蒸馏) · 4
- [交互长视频](#交互长视频) · 9
- [流式系统](#流式系统) · 2
- [具身与世界模型](#具身与世界模型) · 11
- [交互 Avatar](#交互-avatar) · 1
- [智能体与上下文](#智能体与上下文) · 4
- [多模态检索](#多模态检索) · 4
- [评测与可靠性](#评测与可靠性) · 6
- [训练与推理效率](#训练与推理效率) · 2
- [多模态架构与综述](#多模态架构与综述) · 2
- [三维生成与重建](#三维生成与重建) · 2

## 视频生成基础

+ [Connected Self Forcing: Beyond Local Learning in Video Autoregression](<https://arxiv.org/abs/2610.12156>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.12156>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://eastbeanzhang.github.io/CSF>)
  <br>2026-10-08 · 视频生成基础

  <details>
  <summary>brief</summary>

  - **问题**：局部自回归训练截断历史梯度，早期生成难获后续误差信号。
  - **方法**：使用快捷梯度重放连接历史潜变量及注意力缓存。
  - **价值**：在不增加推理开销的情况下改善长视频训练与稳定性。
  - **局限**：训练需要额外重放成本，长时稳定与运动丰富度仍需权衡。

  来源：<a href="https://arxiv.org/abs/2610.12156">[1]</a> · <a href="https://eastbeanzhang.github.io/CSF">[2]</a>
  核验：2026-10-12

  </details>

+ [SGF+: Decoupling Gradient Flows for Autoregressive Video Generation](<https://arxiv.org/abs/2610.10429>)<br>
  [![Star](https://img.shields.io/github/stars/Zihan-Su/Self_Gradient_Forcing_Plus.svg?style=social&label=Star)](<https://github.com/Zihan-Su/Self_Gradient_Forcing_Plus>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.10429>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://zihan-su.github.io/self-gradient-forcing-plus>) [![Weights](https://img.shields.io/badge/Weights-yellow.svg)](<https://huggingface.co/ZihanSu/Self_Gradient_Forcing_Plus>)
  <br>2026-10-07 · 视频生成基础

  <details>
  <summary>brief</summary>

  - **问题**：自回归视频中缓存写入与当前去噪的梯度目标可能冲突。
  - **方法**：分离写入器和去噪器参数，再通过因果注意力联合训练。
  - **价值**：提高长时滚动生成的稳定性，提供可复现代码与权重。
  - **局限**：稳定性可能伴随动态程度降低，固定缓存仍有记忆边界。

  来源：<a href="https://arxiv.org/abs/2610.10429">[1]</a> · <a href="https://github.com/Zihan-Su/Self_Gradient_Forcing_Plus">[2]</a> · <a href="https://huggingface.co/ZihanSu/Self_Gradient_Forcing_Plus">[3]</a> · <a href="https://zihan-su.github.io/self-gradient-forcing-plus">[4]</a>
  核验：2026-10-12

  </details>

+ [Diffusion Forcing: Next-token Prediction Meets Full-Sequence Diffusion](<https://arxiv.org/abs/2407.01392>)<br>
  [![Star](https://img.shields.io/github/stars/buoyancy99/diffusion-forcing.svg?style=social&label=Star)](<https://github.com/buoyancy99/diffusion-forcing>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2407.01392>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://www.boyuan.space/diffusion-forcing>)
  <br>2024-07-01 · 序列建模 / 独立噪声 / 规划

  <details>
  <summary>brief</summary>

  - **问题**：序列预测的灵活长度与整段扩散的引导能力难以兼得。
  - **方法**：训练时为各个序列元素独立设置噪声等级，以因果模型学习不同噪声组合下的去噪。
  - **价值**：统一变长生成、长时序外推和规划引导，为视频及决策提供通用思路。
  - **局限**：原论文使用循环网络；当前主分支已改为时序注意力，复现需区分版本。

  来源：<a href="https://arxiv.org/abs/2407.01392">[1]</a> · <a href="https://github.com/buoyancy99/diffusion-forcing">[2]</a> · <a href="https://www.boyuan.space/diffusion-forcing">[3]</a>
  核验：2026-10-12

  </details>


## 少步蒸馏

+ [Causal Forcing: Autoregressive Diffusion Distillation Done Right for High-Quality Real-Time Interactive Video Generation](<https://arxiv.org/abs/2602.02214>)<br>
  [![Star](https://img.shields.io/github/stars/thu-ml/Causal-Forcing.svg?style=social&label=Star)](<https://github.com/thu-ml/Causal-Forcing>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2602.02214>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://thu-ml.github.io/CausalForcing.github.io>) [![Weights](https://img.shields.io/badge/Weights-yellow.svg)](<https://huggingface.co/zhuhz22/Causal-Forcing/tree/main>)
  <br>2026-02-02 · ODE 初始化 / 交互视频 / 因果教师

  <details>
  <summary>brief</summary>

  - **问题**：双向教师的轨迹初始化与因果学生存在结构不匹配。
  - **方法**：先训练自回归教师，再用因果常微分方程轨迹初始化少步学生，随后进行非对称分布匹配蒸馏。
  - **价值**：改善蒸馏起点，在既定实验设置中提高视频质量与运动表现。
  - **局限**：本条针对原始三阶段方法；后续增强版另有一致性蒸馏，不能混用其结论。

  来源：<a href="https://arxiv.org/abs/2602.02214">[1]</a> · <a href="https://github.com/thu-ml/Causal-Forcing">[2]</a> · <a href="https://huggingface.co/zhuhz22/Causal-Forcing/tree/main">[3]</a> · <a href="https://thu-ml.github.io/CausalForcing.github.io">[4]</a>
  核验：2026-10-12

  </details>

+ [Self Forcing: Bridging the Train-Test Gap in Autoregressive Video Diffusion](<https://arxiv.org/abs/2506.08009>)<br>
  [![Star](https://img.shields.io/github/stars/guandeh17/Self-Forcing.svg?style=social&label=Star)](<https://github.com/guandeh17/Self-Forcing>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2506.08009>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://self-forcing.github.io/>) [![Weights](https://img.shields.io/badge/Weights-yellow.svg)](<https://huggingface.co/gdhe17/Self-Forcing/tree/main>)
  <br>2025-06-09 · 分布匹配 / 自生成历史 / 训练推理对齐

  <details>
  <summary>brief</summary>

  - **问题**：真实历史训练与模型生成历史推理之间的偏差会累积。
  - **方法**：训练中直接自回归展开并缓存自生成历史，用整段视频损失监督，配合少步去噪与随机梯度截断。
  - **价值**：将训练条件贴近部署过程，支持低延迟流式视频生成。
  - **局限**：演示依赖指定硬件与模型设置；长而详细的提示词效果更好，不能外推所有场景。

  来源：<a href="https://arxiv.org/abs/2506.08009">[1]</a> · <a href="https://github.com/guandeh17/Self-Forcing">[2]</a> · <a href="https://huggingface.co/gdhe17/Self-Forcing/tree/main">[3]</a> · <a href="https://self-forcing.github.io/">[4]</a>
  核验：2026-10-12

  </details>

+ [From Slow Bidirectional to Fast Autoregressive Video Diffusion Models](<https://arxiv.org/abs/2412.07772>)<br>
  [![Star](https://img.shields.io/github/stars/tianweiy/CausVid.svg?style=social&label=Star)](<https://github.com/tianweiy/CausVid>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2412.07772>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://causvid.github.io/>) [![Weights](https://img.shields.io/badge/Weights-yellow.svg)](<https://huggingface.co/tianweiy/CausVid/tree/main/autoregressive_checkpoint>)
  <br>2024-12-10 · DMD / KV cache / 自回归

  <details>
  <summary>brief</summary>

  - **问题**：双向视频扩散依赖未来帧，难以低延迟逐帧生成。
  - **方法**：通过教师轨迹初始化、非对称分布匹配蒸馏及因果注意力，将多步模型转为少步自回归生成器。
  - **价值**：结合缓存支持流式生成，并展示动态提示与长视频能力。
  - **局限**：少步生成仍依赖教师质量；公开仓库的示例训练不等同于论文全部实验。

  来源：<a href="https://arxiv.org/abs/2412.07772">[1]</a> · <a href="https://causvid.github.io/">[2]</a> · <a href="https://github.com/tianweiy/CausVid">[3]</a> · <a href="https://huggingface.co/tianweiy/CausVid/tree/main/autoregressive_checkpoint">[4]</a>
  核验：2026-10-12

  </details>

+ [VideoLCM: Video Latent Consistency Model](<https://arxiv.org/abs/2312.09109>)<br>
  [![Star](https://img.shields.io/github/stars/ali-vilab/VGen.svg?style=social&label=Star)](<https://github.com/ali-vilab/VGen>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2312.09109>)
  <br>2023-12-14 · 一致性蒸馏 / 少步采样 / 文生视频 / 潜空间

  <details>
  <summary>brief</summary>

  - **问题**：视频扩散多步采样成本高。
  - **方法**：在潜空间用冻结教师的DDIM轨迹配对和EMA学生目标做一致性蒸馏。
  - **价值**：复用预训练模型，将文生视频压缩至约4–6步，并支持组合条件生成。
  - **局限**：依赖强教师与匹配数据，仍需微调，论文尚未实现实时生成。

  来源：<a href="https://arxiv.org/abs/2312.09109">[1]</a> · <a href="https://arxiv.org/html/2312.09109">[2]</a> · <a href="https://github.com/ali-vilab/VGen">[3]</a>
  核验：2026-10-12

  </details>


## 交互长视频

+ [Memory Forcing: Attendable Mid-Horizon History for Streaming Video Generation](<https://arxiv.org/abs/2610.11756>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.11756>)
  <br>2026-10-08 · 交互长视频

  <details>
  <summary>brief</summary>

  - **问题**：流式视频滑动窗口会丢失中期历史，使早先内容难以延续。
  - **方法**：划分锚点、档案和工作缓存，结合历史选择与分库位置编码。
  - **价值**：在固定缓存预算下增加可访问历史并改善连续性。
  - **局限**：尚非语义检索或持久世界状态，视频帧率不代表生成速度。

  来源：<a href="https://arxiv.org/abs/2610.11756">[1]</a>
  核验：2026-10-12

  </details>

+ [Keepsake: Selective Spatial Memory for Long-Horizon Video Generation](<https://arxiv.org/abs/2610.06588>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.06588>)
  <br>2026-10-05 · 交互长视频

  <details>
  <summary>brief</summary>

  - **问题**：长视频空间记忆随历史增长而膨胀，重复视角挤占有限缓存。
  - **方法**：用姿态与外观图选择固定容量记忆，淘汰可被替代的观测。
  - **价值**：无需重训生成器即可改善长时间空间一致性。
  - **局限**：测试轨迹规模有限，尚不能保证动态场景状态正确。

  来源：<a href="https://arxiv.org/abs/2610.06588">[1]</a>
  核验：2026-10-12

  </details>

+ [LoGo: Local-Global Rewards for Consistent Long-Horizon Video Generation](<https://arxiv.org/abs/2610.03636>)<br>
  [![Star](https://img.shields.io/github/stars/ziqi-ma/logo.svg?style=social&label=Star)](<https://github.com/ziqi-ma/logo>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.03636>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://ziqi-ma.github.io/logo-website>) [![Weights](https://img.shields.io/badge/Weights-yellow.svg)](<https://huggingface.co/ziqima/LoGo>)
  <br>2026-10-02 · 交互长视频

  <details>
  <summary>brief</summary>

  - **问题**：长时视频的局部画面质量与全局三维一致性往往难以兼顾。
  - **方法**：组合局部与全局几何奖励，对视频生成模型进行后训练。
  - **价值**：改善相机运动下场景一致性，并发布训练代码与适配器。
  - **局限**：证据主要来自静态场景，不能外推至动态人体或复杂交互。

  来源：<a href="https://arxiv.org/abs/2610.03636">[1]</a> · <a href="https://github.com/ziqi-ma/logo">[2]</a> · <a href="https://huggingface.co/ziqima/LoGo">[3]</a> · <a href="https://ziqi-ma.github.io/logo-website">[4]</a>
  核验：2026-10-12

  </details>

+ [Weave Forcing: Compositional Memory Routing for Interactive Long Video Generation](<https://arxiv.org/abs/2610.03510>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.03510>)
  <br>2026-10-02 · 交互长视频

  <details>
  <summary>brief</summary>

  - **问题**：交互长视频需要重组历史人物与背景，单一记忆难以匹配。
  - **方法**：以语义槽和区域掩码路由历史缓存，并自适应调整位置编码。
  - **价值**：支持跨镜头组合记忆，增强人物与场景延续性。
  - **局限**：端到端实时性与复杂动态交互仍缺充分验证。

  来源：<a href="https://arxiv.org/abs/2610.03510">[1]</a>
  核验：2026-10-12

  </details>

+ [MosaiChunk: Compositing Spatio-Temporal Memory for Autoregressive Video Generation](<https://arxiv.org/abs/2610.02153>)<br>
  [![Star](https://img.shields.io/github/stars/mosaichunk/MosaiChunk.svg?style=social&label=Star)](<https://github.com/mosaichunk/MosaiChunk>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.02153>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://mosaichunk.github.io/>) [![Weights](https://img.shields.io/badge/Weights-yellow.svg)](<https://huggingface.co/mosaichunk/MosaiChunk>)
  <br>2026-10-01 · 交互长视频

  <details>
  <summary>brief</summary>

  - **问题**：自回归视频有限缓存难以记住离开视野后再次出现的场景。
  - **方法**：冻结生成器，训练轻量路由器组合历史时空片段的注意力缓存。
  - **价值**：在固定活动缓存下增强重访一致性，支持长时记忆检索。
  - **局限**：主机历史存储仍会增长，旧记忆与动态状态冲突尚未解决。

  来源：<a href="https://arxiv.org/abs/2610.02153">[1]</a> · <a href="https://github.com/mosaichunk/MosaiChunk">[2]</a> · <a href="https://huggingface.co/mosaichunk/MosaiChunk">[3]</a> · <a href="https://mosaichunk.github.io/">[4]</a>
  核验：2026-10-12

  </details>

+ [ShotVerse: Advancing Cinematic Camera Control for Text-Driven Multi-Shot Video Creation](<https://arxiv.org/abs/2603.11421>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2603.11421>)
  <br>2026-03-12 · 多镜头视频 / 相机控制 / 轨迹规划

  <details>
  <summary>brief</summary>

  - **问题**：文本镜头描述不够精确，而手工设计跨镜头轨迹成本高。
  - **方法**：将各镜头标定到统一坐标，以同源图文轨迹数据分别训练VLM规划器与相机适配生成器。
  - **价值**：用显式轨迹连接叙事意图和镜头执行，分开评测规划、执行与一致性。
  - **局限**：聚焦整体式多镜头模型的相机控制，不覆盖完整自动制片流程。

  来源：<a href="https://arxiv.org/abs/2603.11421">[1]</a> · <a href="https://arxiv.org/pdf/2603.11421v2">[2]</a>
  核验：2026-10-13

  </details>

+ [Pathwise Test-Time Correction for Autoregressive Long Video Generation](<https://arxiv.org/abs/2602.05871>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2602.05871>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://ttc-1231.github.io/>)
  <br>2026-02-05 · 测试时校正 / 漂移抑制 / 自回归视频

  <details>
  <summary>brief</summary>

  - **问题**：少步自回归视频累积漂移，测试时梯度优化又易破坏蒸馏模型。
  - **方法**：待全局结构稳定后，以首帧条件校正中间预测，再加噪回当前时间步的方差水平。
  - **价值**：无需重训即可干预采样轨迹，作者报告改善30秒生成稳定性。
  - **局限**：依赖初始锚点与随机采样过程；额外校正仍有推理开销。

  来源：<a href="https://arxiv.org/abs/2602.05871">[1]</a> · <a href="https://arxiv.org/pdf/2602.05871v2">[2]</a> · <a href="https://ttc-1231.github.io/">[3]</a>
  核验：2026-10-13

  </details>

+ [Rolling Forcing: Autoregressive Long Video Diffusion in Real Time](<https://arxiv.org/abs/2509.25161>)<br>
  [![Star](https://img.shields.io/github/stars/TencentARC/RollingForcing.svg?style=social&label=Star)](<https://github.com/TencentARC/RollingForcing>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2509.25161>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://kunhao-liu.github.io/Rolling_Forcing_Webpage>) [![Weights](https://img.shields.io/badge/Weights-yellow.svg)](<https://huggingface.co/TencentARC/RollingForcing>)
  <br>2025-09-29 · 注意力锚点 / 滚动窗口 / 长视频

  <details>
  <summary>brief</summary>

  - **问题**：逐帧生成的误差容易在长视频中持续传播。
  - **方法**：在滚动窗口内联合去噪不同噪声等级的帧，保留初始帧缓存作全局锚点，并以非重叠窗口训练。
  - **价值**：在控制训练成本的同时改善长时一致性，展示分钟级实时流式视频。
  - **局限**：联合窗口放宽了相邻帧严格因果性；长视频展示不等于对任意时长的稳定保证。

  来源：<a href="https://arxiv.org/abs/2509.25161">[1]</a> · <a href="https://github.com/TencentARC/RollingForcing">[2]</a> · <a href="https://huggingface.co/TencentARC/RollingForcing">[3]</a> · <a href="https://kunhao-liu.github.io/Rolling_Forcing_Webpage">[4]</a>
  核验：2026-10-12

  </details>

+ [LongLive: Real-time Interactive Long Video Generation](<https://arxiv.org/abs/2509.22622>)<br>
  [![Star](https://img.shields.io/github/stars/NVlabs/LongLive.svg?style=social&label=Star)](<https://github.com/NVlabs/LongLive>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2509.22622>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://nvlabs.github.io/LongLive>) [![Weights](https://img.shields.io/badge/Weights-yellow.svg)](<https://huggingface.co/Efficient-Large-Model/LongLive-1.3B>)
  <br>2025-09-26 · KV recache / 提示词切换 / 长时训练

  <details>
  <summary>brief</summary>

  - **问题**：长视频既要保持一致性，也要及时响应用户提示变化。
  - **方法**：用提示切换时的缓存重算、流式长时训练，以及短窗口注意力和帧锚点维持生成状态。
  - **价值**：将短片模型扩展到可交互的分钟级生成，兼顾响应速度与持续叙事。
  - **局限**：本条对应原始一代论文；速度与时长取决于硬件和配置，不代表任意设备表现。

  来源：<a href="https://arxiv.org/abs/2509.22622">[1]</a> · <a href="https://github.com/NVlabs/LongLive">[2]</a> · <a href="https://huggingface.co/Efficient-Large-Model/LongLive-1.3B">[3]</a> · <a href="https://nvlabs.github.io/LongLive">[4]</a>
  核验：2026-10-12

  </details>


## 流式系统

+ [Real-Time Joint Audio-Video Generation by Parallel Adapter Composition](<https://arxiv.org/abs/2610.10343>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.10343>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://pac-demo-2027.github.io/demo>)
  <br>2026-10-07 · 流式系统

  <details>
  <summary>brief</summary>

  - **问题**：联合音视频生成难以同时获得跨模态同步与少步推理。
  - **方法**：冻结主干，将因果音视频适配器与少步适配器并行组合。
  - **价值**：减少联合重训需求，展示流式音视频生成能力。
  - **局限**：吞吐依赖多卡，首帧延迟和口型漂移仍影响交互体验。

  来源：<a href="https://arxiv.org/abs/2610.10343">[1]</a> · <a href="https://pac-demo-2027.github.io/demo">[2]</a>
  核验：2026-10-12

  </details>

+ [StreamDiffusionV2: A Streaming System for Dynamic and Interactive Video Generation](<https://arxiv.org/abs/2511.07399>)<br>
  [![Star](https://img.shields.io/github/stars/chenfengxu714/StreamDiffusionV2.svg?style=social&label=Star)](<https://github.com/chenfengxu714/StreamDiffusionV2>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2511.07399>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://streamdiffusionv2.github.io/>) [![Weights](https://img.shields.io/badge/Weights-yellow.svg)](<https://huggingface.co/jerryfeng/StreamDiffusionV2>)
  <br>2025-11-10 · 多 GPU / 实时视频 / 系统调度

  <details>
  <summary>brief</summary>

  - **问题**：离线吞吐优化难以满足直播首帧延迟与逐帧截止时间。
  - **方法**：通过延迟目标感知调度、滚动缓存与跨去噪步骤和网络层的流水线组织视频扩散推理。
  - **价值**：无需额外训练即可支持交互视频流和多卡扩展，连接模型与实时服务。
  - **局限**：高帧率报告有特定多卡条件；系统加速不等于底层模型生成能力提升。

  来源：<a href="https://arxiv.org/abs/2511.07399">[1]</a> · <a href="https://github.com/chenfengxu714/StreamDiffusionV2">[2]</a> · <a href="https://huggingface.co/jerryfeng/StreamDiffusionV2">[3]</a> · <a href="https://streamdiffusionv2.github.io/">[4]</a>
  核验：2026-10-12

  </details>


## 具身与世界模型

+ [Dex-One2Many: Learning Dexterous Manipulation from a Single Human Demonstration](<https://arxiv.org/abs/2610.12470>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.12470>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://dex-one2many.github.io/>)
  <br>2026-10-08 · 具身与世界模型

  <details>
  <summary>brief</summary>

  - **问题**：单个人类示范难以覆盖灵巧操作所需的场景与动作变化。
  - **方法**：从视频提取场景图，构造多样仿真初态和奖励并训练强化策略。
  - **价值**：将单次示范扩展为训练任务，支持仿真到真实操作迁移。
  - **局限**：仍需资产、抓取及姿态准备，不代表同一策略零样本跨形态泛化。

  来源：<a href="https://arxiv.org/abs/2610.12470">[1]</a> · <a href="https://dex-one2many.github.io/">[2]</a>
  核验：2026-10-12

  </details>

+ [DreamTrue: Action-Faithful Robot World Model with Counterfactual Post-Training](<https://arxiv.org/abs/2610.12468>)<br>
  [![Star](https://img.shields.io/github/stars/brave-eai/DreamTrue.svg?style=social&label=Star)](<https://github.com/brave-eai/DreamTrue>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.12468>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://brave-eai.github.io/DreamTrue>)
  <br>2026-10-08 · 具身与世界模型

  <details>
  <summary>brief</summary>

  - **问题**：机器人世界模型可能生成视觉合理却不忠实于输入动作的结果。
  - **方法**：结合多视角几何校准、缺陷奖励及反事实强化后训练。
  - **价值**：提高动作条件预测的忠实度，减少违背控制指令的幻觉。
  - **局限**：当前主要验证预测质量，尚不能直接推断实际策略成功率提升。

  来源：<a href="https://arxiv.org/abs/2610.12468">[1]</a> · <a href="https://brave-eai.github.io/DreamTrue">[2]</a> · <a href="https://github.com/brave-eai/DreamTrue">[3]</a>
  核验：2026-10-12

  </details>

+ [RoboRSI: Stable, efficient, and reusable robot self-evolution in complex real-world environments](<https://arxiv.org/abs/2610.12424>)<br>
  [![Star](https://img.shields.io/github/stars/nssmd/RoboRSI.svg?style=social&label=Star)](<https://github.com/nssmd/RoboRSI>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.12424>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://lab.noematrix.ai/blog/2-roborsi>)
  <br>2026-10-08 · 具身与世界模型

  <details>
  <summary>brief</summary>

  - **问题**：复杂真实环境中的机器人需从失败中修正程序并复用经验。
  - **方法**：通过执行反馈迭代代码与技能，在连续任务中积累可用方案。
  - **价值**：展示真实机器人自我改进系统的工程路径和案例。
  - **局限**：运行期间持续开发且存在人工协助，不能视作冻结策略的自主性评测。

  来源：<a href="https://arxiv.org/abs/2610.12424">[1]</a> · <a href="https://github.com/nssmd/RoboRSI">[2]</a> · <a href="https://lab.noematrix.ai/blog/2-roborsi">[3]</a>
  核验：2026-10-12

  </details>

+ [LiteNWM: Efficient Latent World Models for Onboard Visual Navigation in the Wild](<https://arxiv.org/abs/2610.12368>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.12368>)
  <br>2026-10-08 · 具身与世界模型

  <details>
  <summary>brief</summary>

  - **问题**：机载导航需评估多个候选路径，但世界模型计算预算有限。
  - **方法**：共享视觉特征编码，用多时域潜在预测评估候选动作轨迹。
  - **价值**：降低重复编码成本，改善实地视觉导航的路径选择。
  - **局限**：真实测试规模较小，嵌入式推理延迟仍限制快速闭环应用。

  来源：<a href="https://arxiv.org/abs/2610.12368">[1]</a>
  核验：2026-10-12

  </details>

+ [PLaW-VLA: Predictive Latent World Modeling for Vision-Language-Action Policies](<https://arxiv.org/abs/2610.12285>)<br>
  [![Star](https://img.shields.io/github/stars/RainyRobo/PLaW-VLA.svg?style=social&label=Star)](<https://github.com/RainyRobo/PLaW-VLA>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.12285>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://rainyrobo.github.io/PLaW-VLA>)
  <br>2026-10-08 · 具身与世界模型

  <details>
  <summary>brief</summary>

  - **问题**：视觉语言动作策略需要提前感知未来，当前观测不足以规划。
  - **方法**：在冻结视觉编码器空间预测未来状态，由动作专家联合读取。
  - **价值**：将潜在世界预测接入策略训练，实验显示控制表现改善。
  - **局限**：官方预训练权重仍待发布，额外模块耗时不等于端到端延迟。

  来源：<a href="https://arxiv.org/abs/2610.12285">[1]</a> · <a href="https://github.com/RainyRobo/PLaW-VLA">[2]</a> · <a href="https://rainyrobo.github.io/PLaW-VLA">[3]</a>
  核验：2026-10-12

  </details>

+ [RESETTLE: Robotic Recovery through Disagreement-Triggered Retrieval and Efficient Corrective Control](<https://arxiv.org/abs/2610.12185>)<br>
  [![Star](https://img.shields.io/github/stars/JIA-Lab-research/RESETTLE.svg?style=social&label=Star)](<https://github.com/JIA-Lab-research/RESETTLE>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.12185>)
  <br>2026-10-08 · 具身与世界模型

  <details>
  <summary>brief</summary>

  - **问题**：机器人策略遇到失误后缺少可靠的触发机制与恢复控制。
  - **方法**：以动作采样分歧触发成功经验检索，并执行带约束的纠正动作。
  - **价值**：为既有策略增加恢复能力，减少偏离后的连续失败。
  - **局限**：一致但错误的预测可能漏检，模块计时不等于完整系统延迟。

  来源：<a href="https://arxiv.org/abs/2610.12185">[1]</a> · <a href="https://github.com/JIA-Lab-research/RESETTLE">[2]</a>
  核验：2026-10-12

  </details>

+ [UNITAS: A 3D-Native World Action Model for Embodied Manipulation](<https://arxiv.org/abs/2610.12099>)<br>
  [![Star](https://img.shields.io/github/stars/DexForce/UNITAS.svg?style=social&label=Star)](<https://github.com/DexForce/UNITAS>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.12099>)
  <br>2026-10-08 · 具身与世界模型

  <details>
  <summary>brief</summary>

  - **问题**：二维视觉与动作表示分离，难以统一建模空间变化和控制。
  - **方法**：在统一度量空间建模三维场景与动作点轨迹，使用双专家流模型。
  - **价值**：探索三维原生世界动作建模以支持具身操作。
  - **局限**：世界模型带来的独立收益仍有限，完整实现的发布状态需关注。

  来源：<a href="https://arxiv.org/abs/2610.12099">[1]</a> · <a href="https://github.com/DexForce/UNITAS">[2]</a>
  核验：2026-10-12

  </details>

+ [RoboJEPA: Scaling Robotic Latent World Models](<https://arxiv.org/abs/2610.10515>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.10515>)
  <br>2026-10-07 · 具身与世界模型

  <details>
  <summary>brief</summary>

  - **问题**：像素世界模型规划成本高，潜空间模型的规模收益尚待检验。
  - **方法**：扩展机器人潜在预测模型，以目标图像引导闭环动作规划。
  - **价值**：展示大规模潜空间预测用于控制的潜力并优化规划计算。
  - **局限**：多步规划仍有明显延迟，不能直接视为实时控制方案。

  来源：<a href="https://arxiv.org/abs/2610.10515">[1]</a>
  核验：2026-10-12

  </details>

+ [DepthWorld: 3D World Model for Robot Manipulation](<https://arxiv.org/abs/2610.08780>)<br>
  [![Star](https://img.shields.io/github/stars/Jai2500/depthworld.svg?style=social&label=Star)](<https://github.com/Jai2500/depthworld>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.08780>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://jaibardhan.com/depthworld>) [![Weights](https://img.shields.io/badge/Weights-yellow.svg)](<https://huggingface.co/jaibrdhn/depthworld>)
  <br>2026-10-06 · 具身与世界模型

  <details>
  <summary>brief</summary>

  - **问题**：机器人视频世界模型容易产生跨视角不一致的三维几何。
  - **方法**：重新校准多视角数据，联合预测动作条件下的彩色图像与深度。
  - **价值**：改善空间一致性，开放模型权重与标定资源供复现。
  - **局限**：预测质量提升尚不等于策略控制收益，部分数据需申请访问。

  来源：<a href="https://arxiv.org/abs/2610.08780">[1]</a> · <a href="https://github.com/Jai2500/depthworld">[2]</a> · <a href="https://huggingface.co/jaibrdhn/depthworld">[3]</a> · <a href="https://jaibardhan.com/depthworld">[4]</a>
  核验：2026-10-12

  </details>

+ [OpenWAM: An Open Framework for Composable World-Action Models](<https://arxiv.org/abs/2610.07922>)<br>
  [![Star](https://img.shields.io/github/stars/OpenWAM/OpenWAM.svg?style=social&label=Star)](<https://github.com/OpenWAM/OpenWAM>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.07922>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://openwam.stanford.edu/>) [![Weights](https://img.shields.io/badge/Weights-yellow.svg)](<https://huggingface.co/OpenWAM-Stanford/OpenWAM-Pretraining>)
  <br>2026-10-06 · 具身与世界模型

  <details>
  <summary>brief</summary>

  - **问题**：世界模型与动作策略常各自训练，组件难以跨任务组合复用。
  - **方法**：共享因果视频骨干，比较视频动作生成顺序并组合正逆动力学。
  - **价值**：提供统一框架和反事实数据训练路径，便于研究组件复用。
  - **局限**：数据量差异影响归因，仿真复用不等于真实机器人零样本迁移。

  来源：<a href="https://arxiv.org/abs/2610.07922">[1]</a> · <a href="https://github.com/OpenWAM/OpenWAM">[2]</a> · <a href="https://huggingface.co/OpenWAM-Stanford/OpenWAM-Pretraining">[3]</a> · <a href="https://openwam.stanford.edu/">[4]</a>
  核验：2026-10-12

  </details>

+ [PointWAM: 3D World Action Modeling for Dexterous Robotic Manipulation](<https://arxiv.org/abs/2610.02840>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.02840>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://chrockey.github.io/PointWAM>)
  <br>2026-10-02 · 具身与世界模型

  <details>
  <summary>brief</summary>

  - **问题**：灵巧操作需要理解三维场景变化，单纯动作模仿难以迁移。
  - **方法**：联合预测场景点与手部关键点，再将动作重定向到机器人。
  - **价值**：利用人类视频预训练和三维监督连接世界预测与操作。
  - **局限**：依赖重定向及场景准备，精细接触任务的成功率仍有限。

  来源：<a href="https://arxiv.org/abs/2610.02840">[1]</a> · <a href="https://chrockey.github.io/PointWAM">[2]</a>
  核验：2026-10-12

  </details>


## 交互 Avatar

+ [PixReenact: Pixel-Conditioned Causal Video Diffusion for Streaming Head-Avatar Reenactment](<https://arxiv.org/abs/2610.05233>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.05233>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://gavriel-habib.github.io/pixreenact>)
  <br>2026-10-04 · 交互 Avatar

  <details>
  <summary>brief</summary>

  - **问题**：流式头像重演需同时维持身份和跟随驱动视频的头部运动。
  - **方法**：采用像素条件因果扩散、跨身份伪监督及双教师蒸馏。
  - **价值**：以少步分块生成支持低延迟头部头像重演。
  - **局限**：研究范围主要是头部，不等于全身控制或对话交互。

  来源：<a href="https://arxiv.org/abs/2610.05233">[1]</a> · <a href="https://gavriel-habib.github.io/pixreenact">[2]</a>
  核验：2026-10-12

  </details>


## 智能体与上下文

+ [IterSynth: Rethinking Deep Search Agents via Role-Decoupled Iterative Synthesis](<https://arxiv.org/abs/2609.29444>)<br>
  [![Star](https://img.shields.io/github/stars/Tencent/IterSynth.svg?style=social&label=Star)](<https://github.com/Tencent/IterSynth>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2609.29444>)
  <br>2026-09-24 · 摘要状态 / 深度搜索 / 角色解耦

  <details>
  <summary>brief</summary>

  - **问题**：搜索规划与证据综合共用长历史，易受噪声与职责耦合影响。
  - **方法**：同一模型轮流规划和更新摘要，每轮重建上下文，并按角色独立归一化过程奖励。
  - **价值**：8B五项均分50.7，较仅结果奖励高1.8点。
  - **局限**：GAIA低于部分8B基线，摘要遗漏与裁判质量仍是边界。

  来源：<a href="https://arxiv.org/abs/2609.29444">[1]</a> · <a href="https://arxiv.org/pdf/2609.29444v1">[2]</a> · <a href="https://github.com/Tencent/IterSynth">[3]</a>
  核验：2026-10-13

  </details>

+ [From Final Artifacts to Trajectories: Retrospective Process Supervision for Evidence-Grounded Long-Form Generation](<https://arxiv.org/abs/2608.30461>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2608.30461>)
  <br>2026-08-31 · 自训练 / 证据生成 / 过程监督

  <details>
  <summary>brief</summary>

  - **问题**：专家成品丰富，真实检索写作轨迹却稀缺。
  - **方法**：从成品反推任务并实际执行检索，以四维评分过滤，用验证后的合成稿配对轨迹训练。
  - **价值**：同预算对照显示过程监督优于仅模仿最终产物。
  - **局限**：恢复的是合理候选过程；效果依赖成品中可追溯的证据。

  来源：<a href="https://arxiv.org/abs/2608.30461">[1]</a> · <a href="https://arxiv.org/pdf/2608.30461v1">[2]</a>
  核验：2026-10-13

  </details>

+ [ContextPilot: Teaching Agents for Proactive Context Management via Fine-grained RL](<https://arxiv.org/abs/2608.28476>)<br>
  [![Star](https://img.shields.io/github/stars/Tencent/ContextPilot.svg?style=social&label=Star)](<https://github.com/Tencent/ContextPilot>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2608.28476>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://tencent.github.io/ContextPilot>)
  <br>2026-08-28 · 上下文管理 / 分支采样 / 强化学习

  <details>
  <summary>brief</summary>

  - **问题**：长任务中删改上下文的收益难由最终答案奖励准确归因。
  - **方法**：扩展记忆与可恢复折叠工具，按长度和熵变化分支，聚合后继奖励训练轨迹快照。
  - **价值**：8B长问答均分较StateLM提升3.55点。
  - **局限**：依赖专门训练；编码与GUI任务尚未验证。

  来源：<a href="https://arxiv.org/abs/2608.28476">[1]</a> · <a href="https://arxiv.org/pdf/2608.28476v1">[2]</a> · <a href="https://github.com/Tencent/ContextPilot">[3]</a> · <a href="https://tencent.github.io/ContextPilot">[4]</a>
  核验：2026-10-13

  </details>

+ [TRAJDEBUG: Tracing Error Lifecycle to Identify Critical Failures in Long-Horizon Agent Trajectories](<https://arxiv.org/abs/2608.06346>)<br>
  [![Star](https://img.shields.io/github/stars/THU-KEG/TrajDebug.svg?style=social&label=Star)](<https://github.com/THU-KEG/TrajDebug>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2608.06346>)
  <br>2026-08-06 · 轨迹诊断 / 过程反馈 / 错误归因

  <details>
  <summary>brief</summary>

  - **问题**：长轨迹局部错误可能被修复或无害，最早出错不等于失败根因。
  - **方法**：分层压缩历史，以逐字证据识别冲突，按修复状态与终局影响筛选后归因。
  - **价值**：同骨干关键步骤准确率由25.69%升至34.11%。
  - **局限**：漏检会传播，最终归因仍依赖模型判断。

  来源：<a href="https://arxiv.org/abs/2608.06346">[1]</a> · <a href="https://arxiv.org/pdf/2608.06346v1">[2]</a> · <a href="https://github.com/THU-KEG/TrajDebug">[3]</a>
  核验：2026-10-13

  </details>


## 多模态检索

+ [From Saliency to Discriminability: Rank-Preserving Visual Token Pruning for VLM Rerankers](<https://arxiv.org/abs/2609.00667>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2609.00667>)
  <br>2026-09-01 · 排序保持 / 注意力熵 / 视觉裁剪

  <details>
  <summary>brief</summary>

  - **问题**：候选图像的显著区域未必包含决定排序的差异。
  - **方法**：用注意力熵融合查询相关性与跨候选差异，并据此选择分层裁剪位置。
  - **价值**：保留20%视觉词元时，两架构实测加速1.28至1.45倍。
  - **局限**：FashionIQ主表只计首轮命中子集，仍低于未裁剪模型。

  来源：<a href="https://arxiv.org/abs/2609.00667">[1]</a> · <a href="https://arxiv.org/pdf/2609.00667v1">[2]</a>
  核验：2026-10-13

  </details>

+ [SnapBench: Benchmarking Snap-and-Ask Multimodal Retrieval for Mobile Interactions](<https://arxiv.org/abs/2608.29607>)<br>
  [![Star](https://img.shields.io/github/stars/zrchen03/SnapBench.svg?style=social&label=Star)](<https://github.com/zrchen03/SnapBench>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2608.29607>)
  <br>2026-08-30 · 拍照问答 / 模态融合 / 鲁棒检索

  <details>
  <summary>brief</summary>

  - **问题**：拍照问答的图文噪声与粗粒度文本可能共同损害实体检索。
  - **方法**：固定目标及图库构造成对扰动，按图像排序一致性和分数方差自适应融合。
  - **价值**：揭示文本稀释视觉排序及联合扰动的非加性影响。
  - **局限**：1145查询且扰动为程序合成，不能替代真实上传分布评估。

  来源：<a href="https://arxiv.org/abs/2608.29607">[1]</a> · <a href="https://arxiv.org/pdf/2608.29607v1">[2]</a> · <a href="https://github.com/zrchen03/SnapBench">[3]</a>
  核验：2026-10-13

  </details>

+ [RePair: Turning Retrieval Failures into Counterfactual Hard Pairs](<https://arxiv.org/abs/2608.29604>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2608.29604>)
  <br>2026-08-30 · 反事实数据 / 困难样本 / 对比学习

  <details>
  <summary>brief</summary>

  - **问题**：通用数据增强不一定修复检索器当前的近邻语义混淆。
  - **方法**：双向挖掘并核验误召回，最小反事实编辑后组织3×3局部对比网格，保留原始全局损失。
  - **价值**：同预算消融支持失败定位与局部配对的贡献。
  - **局限**：仅单次模型快照挖掘，跨数据集迁移及融合式检索器未验证。

  来源：<a href="https://arxiv.org/abs/2608.29604">[1]</a> · <a href="https://arxiv.org/pdf/2608.29604v1">[2]</a>
  核验：2026-10-13

  </details>

+ [EviRank: Structured Relevance Evidence for Multimodal Image Re-ranking](<https://arxiv.org/abs/2608.20886>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2608.20886>)
  <br>2026-08-21 · 结构化证据 / 蒸馏 / 重排序

  <details>
  <summary>brief</summary>

  - **问题**：图像重排序易忽略组合查询中的细粒度约束。
  - **方法**：以六类语义槽表示必需、禁止及可忽略条件，先规则评分再局部列表比较。
  - **价值**：消融支持约束分解的作用，学生可脱离教师部署。
  - **局限**：效果受首轮候选覆盖限制，实验主要为英文静态图像。

  来源：<a href="https://arxiv.org/abs/2608.20886">[1]</a> · <a href="https://arxiv.org/pdf/2608.20886v1">[2]</a>
  核验：2026-10-13

  </details>


## 评测与可靠性

+ [Can LLM-as-a-Judge Reliably Verify Rubrics in Agentic Scenarios?](<https://arxiv.org/abs/2606.29920>)<br>
  [![Star](https://img.shields.io/github/stars/THU-KEG/RuVerBench.svg?style=social&label=Star)](<https://github.com/THU-KEG/RuVerBench>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2606.29920>)
  <br>2026-06-29 · 智能体评测 / 模型裁判 / 评分细则

  <details>
  <summary>brief</summary>

  - **问题**：研究报告与代码轨迹中的评分细则难以被模型可靠核验。
  - **方法**：人工双重标注并裁决2458个输出与细则配对，按类别宏平均平衡准确率评估。
  - **价值**：揭示代码轨迹比报告更难，批量核验存在效率与准确性权衡。
  - **局限**：已剔除含糊及缺证据细则，不能代表全部线上评审。

  来源：<a href="https://arxiv.org/abs/2606.29920">[1]</a> · <a href="https://arxiv.org/pdf/2606.29920v2">[2]</a> · <a href="https://github.com/THU-KEG/RuVerBench">[3]</a>
  核验：2026-10-13

  </details>

+ [Summarization is Not Dead Yet](<https://arxiv.org/abs/2606.08000>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2606.08000>)
  <br>2026-06-06 · 事实性 / 人工评测 / 文本摘要

  <details>
  <summary>brief</summary>

  - **问题**：整体偏好容易把摘要流畅度与信息充分性混为一谈。
  - **方法**：结合分维人工盲评、排除自评的模型裁判、外部事实核验与语言学分析。
  - **价值**：五数据集上人工摘要保有信息和忠实性优势。
  - **局限**：仅五个通用模型的零样本快照；外部事实正确不等于遵守仅据原文要求。

  来源：<a href="https://arxiv.org/abs/2606.08000">[1]</a> · <a href="https://arxiv.org/pdf/2606.08000v3">[2]</a>
  核验：2026-10-13

  </details>

+ [RedEdit: Agentic Red-Teaming of Image Safety Classifiers via MCTS-Guided Photo-Editing](<https://arxiv.org/abs/2606.06140>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2606.06140>)
  <br>2026-06-04 · 图像安全 / 红队测试 / 鲁棒评测

  <details>
  <summary>brief</summary>

  - **问题**：图像审核器对常见照片编辑的稳健性缺少系统评测。
  - **方法**：用视觉模型提议与树搜索组织编辑序列，同时核验检测结果和内容保留。
  - **价值**：为审核防御提供跨检测器失效诊断。
  - **局限**：76.2%来自原本被拦截的164张中125张，非全部777张；编辑深度不等于查询次数。

  来源：<a href="https://arxiv.org/abs/2606.06140">[1]</a> · <a href="https://arxiv.org/pdf/2606.06140v1">[2]</a>
  核验：2026-10-13

  </details>

+ [DSH-Bench: A Difficulty- and Scenario-Aware Benchmark with Hierarchical Subject Taxonomy for Subject-Driven Text-to-Image Generation](<https://arxiv.org/abs/2603.08090>)<br>
  [![Star](https://img.shields.io/github/stars/sunriverhzy/DSH-Bench.svg?style=social&label=Star)](<https://github.com/sunriverhzy/DSH-Bench>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2603.08090>)
  <br>2026-03-09 · 主体生成 / 分层评测 / 身份一致性

  <details>
  <summary>brief</summary>

  - **问题**：主体生成的总分掩盖复杂主体与不同指令场景的能力差异。
  - **方法**：按层级采样58类主体，交叉划分难度与场景，以人工评分及解释微调Qwen裁判。
  - **价值**：把主体保持、指令遵循和画质分开诊断，定位细节重建短板。
  - **局限**：聚焦单主体；身份保持与属性改写存在权衡，不能外推多主体交互。

  来源：<a href="https://arxiv.org/abs/2603.08090">[1]</a> · <a href="https://arxiv.org/pdf/2603.08090v3">[2]</a> · <a href="https://github.com/sunriverhzy/DSH-Bench">[3]</a>
  核验：2026-10-13

  </details>

+ [Purify then Guide: Rethinking Domain Generalization for Multimodal Face Anti-Spoofing](<https://arxiv.org/abs/2505.09484>)<br>
  [![Star](https://img.shields.io/github/stars/murInJ/MMDA.svg?style=social&label=Star)](<https://github.com/murInJ/MMDA>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2505.09484>)
  <br>2025-05-14 · 人脸反欺骗 / 多模态 / 跨域泛化

  <details>
  <summary>brief</summary>

  - **问题**：直接对齐多模态特征会同时对齐伪造线索和域偏差。
  - **方法**：以同域异样本差分抑制共有噪声，再软对齐多提示语义子空间，并用U形适配保留CLIP结构。
  - **价值**：将去噪、语义引导与任务适配分开处理，兼顾缺失模态场景。
  - **局限**：依赖同域共享偏差的建模假设；基准收益不等于开放环境安全保证。

  来源：<a href="https://arxiv.org/abs/2505.09484">[1]</a> · <a href="https://arxiv.org/pdf/2505.09484v2">[2]</a> · <a href="https://github.com/murInJ/MMDA">[3]</a>
  核验：2026-10-13

  </details>

+ [FactGuard: Leveraging Multi-Agent Systems to Generate Answerable and Unanswerable Questions for Enhanced Long-Context LLM Extraction](<https://arxiv.org/abs/2504.05607>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2504.05607>)
  <br>2025-04-08 · 公开初版 / 拒答 / 长上下文

  <details>
  <summary>brief</summary>

  - **问题**：长文问答常把相关但不足的证据误作可回答依据。
  - **方法**：筛选文本片段生成证据问答，再删除证据或改写错误前提，并检索复查冲突答案。
  - **价值**：区分缺失与误导证据，支持诊断拒答能力。
  - **局限**：本条据2025年公开初版；不能套用后续稿的11模型及71.62%结论。

  来源：<a href="https://arxiv.org/abs/2504.05607">[1]</a> · <a href="https://arxiv.org/pdf/2504.05607v1">[2]</a>
  核验：2026-10-13

  </details>


## 训练与推理效率

+ [HyQuant: Hybrid-Precision Quantization for LLM Attention](<https://arxiv.org/abs/2608.27875>)<br>
  [![Star](https://img.shields.io/github/stars/jerrysfls/HyQuant.svg?style=social&label=Star)](<https://github.com/jerrysfls/HyQuant>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2608.27875>)
  <br>2026-08-28 · KV缓存 / 注意力量化 / 混合精度

  <details>
  <summary>brief</summary>

  - **问题**：均匀低比特量化会放大高注意力位置的误差。
  - **方法**：保留高列注意力词元和局部窗口为高精度，将其余KV量化并融合反量化计算。
  - **价值**：在所测模型上接近全精度，减轻长上下文显存压力。
  - **局限**：32K内核加速3.58倍但端到端仅1.17倍，依赖H100设置。

  来源：<a href="https://arxiv.org/abs/2608.27875">[1]</a> · <a href="https://arxiv.org/pdf/2608.27875v3">[2]</a> · <a href="https://github.com/jerrysfls/HyQuant">[3]</a>
  核验：2026-10-13

  </details>

+ [KDFlow: A User-Friendly and Efficient Knowledge Distillation Framework for Large Language Models](<https://arxiv.org/abs/2603.01875>)<br>
  [![Star](https://img.shields.io/github/stars/songmzhang/KDFlow.svg?style=social&label=Star)](<https://github.com/songmzhang/KDFlow>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2603.01875>)
  <br>2026-03-02 · 知识蒸馏 / 训推解耦 / 通信优化

  <details>
  <summary>brief</summary>

  - **问题**：教师推理与学生训练共用后端低效，全词表输出传输昂贵。
  - **方法**：教师由SGLang执行，仅传末层隐状态，在FSDP2学生侧重算完整输出分布。
  - **价值**：保持蒸馏损失并降低通信，离线实验加速1.44至6.36倍。
  - **局限**：上限采用FP8教师；超64卡扩展与异步训练尚未验证。

  来源：<a href="https://arxiv.org/abs/2603.01875">[1]</a> · <a href="https://arxiv.org/pdf/2603.01875v4">[2]</a> · <a href="https://github.com/songmzhang/KDFlow">[3]</a>
  核验：2026-10-13

  </details>


## 多模态架构与综述

+ [A Survey on Rubric-Guided Reinforcement Learning for Language Models](<https://arxiv.org/abs/2608.27505>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2608.27505>)
  <br>2026-08-27 · 奖励投机 / 强化学习 / 评分细则

  <details>
  <summary>brief</summary>

  - **问题**：自然语言奖励细则的歧义、粒度与语义漂移影响强化学习。
  - **方法**：以先验和条件化细则组织方法，并建议在固定参考集上监测评分秩相关衰减。
  - **价值**：区分逐步监督与原子清单，为奖励审计提供思路。
  - **局限**：贝叶斯表述是分析抽象，多数方法没有精确推断保证或统一对照。

  来源：<a href="https://arxiv.org/abs/2608.27505">[1]</a> · <a href="https://arxiv.org/pdf/2608.27505v2">[2]</a>
  核验：2026-10-13

  </details>

+ [Toward Native Multimodal Modeling: A Roadmap](<https://arxiv.org/abs/2605.25343>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2605.25343>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://nmm-roadmap.github.io/>)
  <br>2026-05-25 · 原生多模态 / 流式交互 / 理解与生成

  <details>
  <summary>brief</summary>

  - **问题**：原生多模态的融合深度与输入输出能力缺少统一描述。
  - **方法**：交叉梳理中早期融合与三类模态流，比较离散统一和保留模态特性的路线。
  - **价值**：串联数据配比、训练、流式部署，并提出质量与响应时机联合评测。
  - **局限**：属分类与路线展望，未以受控实验确立早期融合的普遍优势。

  来源：<a href="https://arxiv.org/abs/2605.25343">[1]</a> · <a href="https://arxiv.org/pdf/2605.25343v1">[2]</a> · <a href="https://nmm-roadmap.github.io/">[3]</a>
  核验：2026-10-13

  </details>


## 三维生成与重建

+ [OmniX: Any-view and Any-time 4D Reconstruction via Feed-forward Trajectory Fields](<https://arxiv.org/abs/2607.10840>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2607.10840>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://omnix4d.github.io/>)
  <br>2026-07-12 · 四维重建 / 点轨迹 / 稀疏注意力

  <details>
  <summary>brief</summary>

  - **问题**：静态几何与动态对应混合建模，妨碍大幅视角变化下的四维重建。
  - **方法**：用少量动态词元与稀疏时空注意力分离运动，再以可变形采样头输出逐像素轨迹。
  - **价值**：一次前馈整合跨视角和时刻观测，配套UE5几何标注数据。
  - **局限**：方法利用运动稀疏低秩假设；并非直接生成可渲染的动态资产。

  来源：<a href="https://arxiv.org/abs/2607.10840">[1]</a> · <a href="https://arxiv.org/pdf/2607.10840v1">[2]</a> · <a href="https://omnix4d.github.io/">[3]</a>
  核验：2026-10-13

  </details>

+ [EditVerse3D: High-Quality 3D Object Editing with Region-Aware Learning](<https://arxiv.org/abs/2607.07187>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2607.07187>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://editverse3d.github.io/>)
  <br>2026-07-08 · 三维编辑 / 区域自适应 / 粗框引导

  <details>
  <summary>brief</summary>

  - **问题**：精确掩码与多视图编辑流程增加三维局部修改的操作成本。
  - **方法**：基于TRELLIS输入粗三维框和参考图，自适应加权难学区域，以移除再恢复部件构造训练对。
  - **价值**：将编辑区学习与保留区约束结合，降低精细标注要求。
  - **局限**：训练以添加编辑为主；仍需输入三维对象、区域框和目标图。

  来源：<a href="https://arxiv.org/abs/2607.07187">[1]</a> · <a href="https://arxiv.org/pdf/2607.07187v2">[2]</a> · <a href="https://editverse3d.github.io/">[3]</a>
  核验：2026-10-13

  </details>

## 维护

Python 3.9+，无第三方依赖。

```bash
python3 scripts/paper_watch.py validate
python3 scripts/paper_watch.py build --check
python3 -m unittest discover -s tests -v
node --test tests/reader.test.cjs
```

数据和源码公开；不收录 PDF、私人笔记、实验记录或会话原文。推送到 main 后自动验证并部署在线阅读页及离线 ZIP。云端研究任务的接入状态见 [接入说明](docs/INTEGRATION.md)。

组织形式参考 [Awesome-Video-Diffusion](https://github.com/showlab/Awesome-Video-Diffusion)。摘要为本项目独立撰写；论文、模型和源码的使用条件以各原始发布方为准。

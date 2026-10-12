# Research Paper Watch

公开论文精选：视频生成、交互 Avatar、具身与世界模型。每篇附可折叠中文简介与一手来源。

**28 篇论文** · [在线阅读（支持快捷键）](https://ripemangobox.github.io/research-paper-watch/) · [下载离线阅读器 ZIP](https://ripemangobox.github.io/research-paper-watch/research-paper-watch.zip) · [唯一数据源](data/papers.json) · [导入与任务接入](docs/INTEGRATION.md)

在线阅读页直接支持搜索、分类、E 全部展开、C 全部收起。离线 ZIP 解压后双击 index.html，无需安装或启动服务器。GitHub README 不运行自定义脚本：可点击简介，或 Tab 聚焦后按 Enter / 空格展开收起；E / C 请使用在线阅读页。

日期为论文首次公开日期；空链接表示尚未核实。简介中的局限包含基于公开证据的阅读边界，不代表作者自述的缺陷。

## 目录

- [视频生成基础](#视频生成基础) · 3
- [少步蒸馏](#少步蒸馏) · 4
- [交互长视频](#交互长视频) · 7
- [流式系统](#流式系统) · 2
- [具身与世界模型](#具身与世界模型) · 11
- [交互 Avatar](#交互 Avatar) · 1

## 视频生成基础

+ [Connected Self Forcing: Beyond Local Learning in Video Autoregression](<https://arxiv.org/abs/2610.12156>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.12156>) [![Website](https://img.shields.io/badge/Website-9cf.svg)](<https://eastbeanzhang.github.io/CSF>)
  <br>2026-10-08 · 视频生成基础

  <details>
  <summary>中文简介：问题 · 方法 · 价值 · 局限</summary>

  - **问题**：局部自回归训练截断历史梯度，早期生成难获后续误差信号。
  - **方法**：使用快捷梯度重放连接历史潜变量及注意力缓存。
  - **价值**：在不增加推理开销的情况下改善长视频训练与稳定性。
  - **局限**：训练需要额外重放成本，长时稳定与运动丰富度仍需权衡。

  来源：<a href="https://arxiv.org/abs/2610.12156">[1]</a> · <a href="https://eastbeanzhang.github.io/CSF">[2]</a>
  核验：2026-10-12

  </details>

+ [SGF+: Decoupling Gradient Flows for Autoregressive Video Generation](<https://arxiv.org/abs/2610.10429>)<br>
  [![Star](https://img.shields.io/github/stars/Zihan-Su/Self_Gradient_Forcing_Plus.svg?style=social&label=Star)](<https://github.com/Zihan-Su/Self_Gradient_Forcing_Plus>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.10429>) [![Website](https://img.shields.io/badge/Website-9cf.svg)](<https://zihan-su.github.io/self-gradient-forcing-plus>) [![Weights](https://img.shields.io/badge/Weights-yellow.svg)](<https://huggingface.co/ZihanSu/Self_Gradient_Forcing_Plus>)
  <br>2026-10-07 · 视频生成基础

  <details>
  <summary>中文简介：问题 · 方法 · 价值 · 局限</summary>

  - **问题**：自回归视频中缓存写入与当前去噪的梯度目标可能冲突。
  - **方法**：分离写入器和去噪器参数，再通过因果注意力联合训练。
  - **价值**：提高长时滚动生成的稳定性，提供可复现代码与权重。
  - **局限**：稳定性可能伴随动态程度降低，固定缓存仍有记忆边界。

  来源：<a href="https://arxiv.org/abs/2610.10429">[1]</a> · <a href="https://github.com/Zihan-Su/Self_Gradient_Forcing_Plus">[2]</a> · <a href="https://huggingface.co/ZihanSu/Self_Gradient_Forcing_Plus">[3]</a> · <a href="https://zihan-su.github.io/self-gradient-forcing-plus">[4]</a>
  核验：2026-10-12

  </details>

+ [Diffusion Forcing: Next-token Prediction Meets Full-Sequence Diffusion](<https://arxiv.org/abs/2407.01392>)<br>
  [![Star](https://img.shields.io/github/stars/buoyancy99/diffusion-forcing.svg?style=social&label=Star)](<https://github.com/buoyancy99/diffusion-forcing>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2407.01392>) [![Website](https://img.shields.io/badge/Website-9cf.svg)](<https://www.boyuan.space/diffusion-forcing>)
  <br>2024-07-01 · 序列建模 / 独立噪声 / 规划

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

+ [Causal Forcing: Autoregressive Diffusion Distillation Done Right for High-Quality Real-Time Interactive Video Generation](<https://arxiv.org/abs/2602.02214>)<br>
  [![Star](https://img.shields.io/github/stars/thu-ml/Causal-Forcing.svg?style=social&label=Star)](<https://github.com/thu-ml/Causal-Forcing>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2602.02214>) [![Website](https://img.shields.io/badge/Website-9cf.svg)](<https://thu-ml.github.io/CausalForcing.github.io>) [![Weights](https://img.shields.io/badge/Weights-yellow.svg)](<https://huggingface.co/zhuhz22/Causal-Forcing/tree/main>)
  <br>2026-02-02 · ODE 初始化 / 交互视频 / 因果教师

  <details>
  <summary>中文简介：问题 · 方法 · 价值 · 局限</summary>

  - **问题**：双向教师的轨迹初始化与因果学生存在结构不匹配。
  - **方法**：先训练自回归教师，再用因果常微分方程轨迹初始化少步学生，随后进行非对称分布匹配蒸馏。
  - **价值**：改善蒸馏起点，在既定实验设置中提高视频质量与运动表现。
  - **局限**：本条针对原始三阶段方法；后续增强版另有一致性蒸馏，不能混用其结论。

  来源：<a href="https://arxiv.org/abs/2602.02214">[1]</a> · <a href="https://github.com/thu-ml/Causal-Forcing">[2]</a> · <a href="https://huggingface.co/zhuhz22/Causal-Forcing/tree/main">[3]</a> · <a href="https://thu-ml.github.io/CausalForcing.github.io">[4]</a>
  核验：2026-10-12

  </details>

+ [Self Forcing: Bridging the Train-Test Gap in Autoregressive Video Diffusion](<https://arxiv.org/abs/2506.08009>)<br>
  [![Star](https://img.shields.io/github/stars/guandeh17/Self-Forcing.svg?style=social&label=Star)](<https://github.com/guandeh17/Self-Forcing>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2506.08009>) [![Website](https://img.shields.io/badge/Website-9cf.svg)](<https://self-forcing.github.io/>) [![Weights](https://img.shields.io/badge/Weights-yellow.svg)](<https://huggingface.co/gdhe17/Self-Forcing/tree/main>)
  <br>2025-06-09 · 分布匹配 / 自生成历史 / 训练推理对齐

  <details>
  <summary>中文简介：问题 · 方法 · 价值 · 局限</summary>

  - **问题**：真实历史训练与模型生成历史推理之间的偏差会累积。
  - **方法**：训练中直接自回归展开并缓存自生成历史，用整段视频损失监督，配合少步去噪与随机梯度截断。
  - **价值**：将训练条件贴近部署过程，支持低延迟流式视频生成。
  - **局限**：演示依赖指定硬件与模型设置；长而详细的提示词效果更好，不能外推所有场景。

  来源：<a href="https://arxiv.org/abs/2506.08009">[1]</a> · <a href="https://github.com/guandeh17/Self-Forcing">[2]</a> · <a href="https://huggingface.co/gdhe17/Self-Forcing/tree/main">[3]</a> · <a href="https://self-forcing.github.io/">[4]</a>
  核验：2026-10-12

  </details>

+ [From Slow Bidirectional to Fast Autoregressive Video Diffusion Models](<https://arxiv.org/abs/2412.07772>)<br>
  [![Star](https://img.shields.io/github/stars/tianweiy/CausVid.svg?style=social&label=Star)](<https://github.com/tianweiy/CausVid>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2412.07772>) [![Website](https://img.shields.io/badge/Website-9cf.svg)](<https://causvid.github.io/>) [![Weights](https://img.shields.io/badge/Weights-yellow.svg)](<https://huggingface.co/tianweiy/CausVid/tree/main/autoregressive_checkpoint>)
  <br>2024-12-10 · DMD / KV cache / 自回归

  <details>
  <summary>中文简介：问题 · 方法 · 价值 · 局限</summary>

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
  <summary>中文简介：问题 · 方法 · 价值 · 局限</summary>

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
  <summary>中文简介：问题 · 方法 · 价值 · 局限</summary>

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
  <summary>中文简介：问题 · 方法 · 价值 · 局限</summary>

  - **问题**：长视频空间记忆随历史增长而膨胀，重复视角挤占有限缓存。
  - **方法**：用姿态与外观图选择固定容量记忆，淘汰可被替代的观测。
  - **价值**：无需重训生成器即可改善长时间空间一致性。
  - **局限**：测试轨迹规模有限，尚不能保证动态场景状态正确。

  来源：<a href="https://arxiv.org/abs/2610.06588">[1]</a>
  核验：2026-10-12

  </details>

+ [LoGo: Local-Global Rewards for Consistent Long-Horizon Video Generation](<https://arxiv.org/abs/2610.03636>)<br>
  [![Star](https://img.shields.io/github/stars/ziqi-ma/logo.svg?style=social&label=Star)](<https://github.com/ziqi-ma/logo>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.03636>) [![Website](https://img.shields.io/badge/Website-9cf.svg)](<https://ziqi-ma.github.io/logo-website>) [![Weights](https://img.shields.io/badge/Weights-yellow.svg)](<https://huggingface.co/ziqima/LoGo>)
  <br>2026-10-02 · 交互长视频

  <details>
  <summary>中文简介：问题 · 方法 · 价值 · 局限</summary>

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
  <summary>中文简介：问题 · 方法 · 价值 · 局限</summary>

  - **问题**：交互长视频需要重组历史人物与背景，单一记忆难以匹配。
  - **方法**：以语义槽和区域掩码路由历史缓存，并自适应调整位置编码。
  - **价值**：支持跨镜头组合记忆，增强人物与场景延续性。
  - **局限**：端到端实时性与复杂动态交互仍缺充分验证。

  来源：<a href="https://arxiv.org/abs/2610.03510">[1]</a>
  核验：2026-10-12

  </details>

+ [MosaiChunk: Compositing Spatio-Temporal Memory for Autoregressive Video Generation](<https://arxiv.org/abs/2610.02153>)<br>
  [![Star](https://img.shields.io/github/stars/mosaichunk/MosaiChunk.svg?style=social&label=Star)](<https://github.com/mosaichunk/MosaiChunk>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.02153>) [![Website](https://img.shields.io/badge/Website-9cf.svg)](<https://mosaichunk.github.io/>) [![Weights](https://img.shields.io/badge/Weights-yellow.svg)](<https://huggingface.co/mosaichunk/MosaiChunk>)
  <br>2026-10-01 · 交互长视频

  <details>
  <summary>中文简介：问题 · 方法 · 价值 · 局限</summary>

  - **问题**：自回归视频有限缓存难以记住离开视野后再次出现的场景。
  - **方法**：冻结生成器，训练轻量路由器组合历史时空片段的注意力缓存。
  - **价值**：在固定活动缓存下增强重访一致性，支持长时记忆检索。
  - **局限**：主机历史存储仍会增长，旧记忆与动态状态冲突尚未解决。

  来源：<a href="https://arxiv.org/abs/2610.02153">[1]</a> · <a href="https://github.com/mosaichunk/MosaiChunk">[2]</a> · <a href="https://huggingface.co/mosaichunk/MosaiChunk">[3]</a> · <a href="https://mosaichunk.github.io/">[4]</a>
  核验：2026-10-12

  </details>

+ [Rolling Forcing: Autoregressive Long Video Diffusion in Real Time](<https://arxiv.org/abs/2509.25161>)<br>
  [![Star](https://img.shields.io/github/stars/TencentARC/RollingForcing.svg?style=social&label=Star)](<https://github.com/TencentARC/RollingForcing>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2509.25161>) [![Website](https://img.shields.io/badge/Website-9cf.svg)](<https://kunhao-liu.github.io/Rolling_Forcing_Webpage>) [![Weights](https://img.shields.io/badge/Weights-yellow.svg)](<https://huggingface.co/TencentARC/RollingForcing>)
  <br>2025-09-29 · 注意力锚点 / 滚动窗口 / 长视频

  <details>
  <summary>中文简介：问题 · 方法 · 价值 · 局限</summary>

  - **问题**：逐帧生成的误差容易在长视频中持续传播。
  - **方法**：在滚动窗口内联合去噪不同噪声等级的帧，保留初始帧缓存作全局锚点，并以非重叠窗口训练。
  - **价值**：在控制训练成本的同时改善长时一致性，展示分钟级实时流式视频。
  - **局限**：联合窗口放宽了相邻帧严格因果性；长视频展示不等于对任意时长的稳定保证。

  来源：<a href="https://arxiv.org/abs/2509.25161">[1]</a> · <a href="https://github.com/TencentARC/RollingForcing">[2]</a> · <a href="https://huggingface.co/TencentARC/RollingForcing">[3]</a> · <a href="https://kunhao-liu.github.io/Rolling_Forcing_Webpage">[4]</a>
  核验：2026-10-12

  </details>

+ [LongLive: Real-time Interactive Long Video Generation](<https://arxiv.org/abs/2509.22622>)<br>
  [![Star](https://img.shields.io/github/stars/NVlabs/LongLive.svg?style=social&label=Star)](<https://github.com/NVlabs/LongLive>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2509.22622>) [![Website](https://img.shields.io/badge/Website-9cf.svg)](<https://nvlabs.github.io/LongLive>) [![Weights](https://img.shields.io/badge/Weights-yellow.svg)](<https://huggingface.co/Efficient-Large-Model/LongLive-1.3B>)
  <br>2025-09-26 · KV recache / 提示词切换 / 长时训练

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

+ [Real-Time Joint Audio-Video Generation by Parallel Adapter Composition](<https://arxiv.org/abs/2610.10343>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.10343>) [![Website](https://img.shields.io/badge/Website-9cf.svg)](<https://pac-demo-2027.github.io/demo>)
  <br>2026-10-07 · 流式系统

  <details>
  <summary>中文简介：问题 · 方法 · 价值 · 局限</summary>

  - **问题**：联合音视频生成难以同时获得跨模态同步与少步推理。
  - **方法**：冻结主干，将因果音视频适配器与少步适配器并行组合。
  - **价值**：减少联合重训需求，展示流式音视频生成能力。
  - **局限**：吞吐依赖多卡，首帧延迟和口型漂移仍影响交互体验。

  来源：<a href="https://arxiv.org/abs/2610.10343">[1]</a> · <a href="https://pac-demo-2027.github.io/demo">[2]</a>
  核验：2026-10-12

  </details>

+ [StreamDiffusionV2: A Streaming System for Dynamic and Interactive Video Generation](<https://arxiv.org/abs/2511.07399>)<br>
  [![Star](https://img.shields.io/github/stars/chenfengxu714/StreamDiffusionV2.svg?style=social&label=Star)](<https://github.com/chenfengxu714/StreamDiffusionV2>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2511.07399>) [![Website](https://img.shields.io/badge/Website-9cf.svg)](<https://streamdiffusionv2.github.io/>) [![Weights](https://img.shields.io/badge/Weights-yellow.svg)](<https://huggingface.co/jerryfeng/StreamDiffusionV2>)
  <br>2025-11-10 · 多 GPU / 实时视频 / 系统调度

  <details>
  <summary>中文简介：问题 · 方法 · 价值 · 局限</summary>

  - **问题**：离线吞吐优化难以满足直播首帧延迟与逐帧截止时间。
  - **方法**：通过延迟目标感知调度、滚动缓存与跨去噪步骤和网络层的流水线组织视频扩散推理。
  - **价值**：无需额外训练即可支持交互视频流和多卡扩展，连接模型与实时服务。
  - **局限**：高帧率报告有特定多卡条件；系统加速不等于底层模型生成能力提升。

  来源：<a href="https://arxiv.org/abs/2511.07399">[1]</a> · <a href="https://github.com/chenfengxu714/StreamDiffusionV2">[2]</a> · <a href="https://huggingface.co/jerryfeng/StreamDiffusionV2">[3]</a> · <a href="https://streamdiffusionv2.github.io/">[4]</a>
  核验：2026-10-12

  </details>


## 具身与世界模型

+ [Dex-One2Many: Learning Dexterous Manipulation from a Single Human Demonstration](<https://arxiv.org/abs/2610.12470>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.12470>) [![Website](https://img.shields.io/badge/Website-9cf.svg)](<https://dex-one2many.github.io/>)
  <br>2026-10-08 · 具身与世界模型

  <details>
  <summary>中文简介：问题 · 方法 · 价值 · 局限</summary>

  - **问题**：单个人类示范难以覆盖灵巧操作所需的场景与动作变化。
  - **方法**：从视频提取场景图，构造多样仿真初态和奖励并训练强化策略。
  - **价值**：将单次示范扩展为训练任务，支持仿真到真实操作迁移。
  - **局限**：仍需资产、抓取及姿态准备，不代表同一策略零样本跨形态泛化。

  来源：<a href="https://arxiv.org/abs/2610.12470">[1]</a> · <a href="https://dex-one2many.github.io/">[2]</a>
  核验：2026-10-12

  </details>

+ [DreamTrue: Action-Faithful Robot World Model with Counterfactual Post-Training](<https://arxiv.org/abs/2610.12468>)<br>
  [![Star](https://img.shields.io/github/stars/brave-eai/DreamTrue.svg?style=social&label=Star)](<https://github.com/brave-eai/DreamTrue>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.12468>) [![Website](https://img.shields.io/badge/Website-9cf.svg)](<https://brave-eai.github.io/DreamTrue>)
  <br>2026-10-08 · 具身与世界模型

  <details>
  <summary>中文简介：问题 · 方法 · 价值 · 局限</summary>

  - **问题**：机器人世界模型可能生成视觉合理却不忠实于输入动作的结果。
  - **方法**：结合多视角几何校准、缺陷奖励及反事实强化后训练。
  - **价值**：提高动作条件预测的忠实度，减少违背控制指令的幻觉。
  - **局限**：当前主要验证预测质量，尚不能直接推断实际策略成功率提升。

  来源：<a href="https://arxiv.org/abs/2610.12468">[1]</a> · <a href="https://brave-eai.github.io/DreamTrue">[2]</a> · <a href="https://github.com/brave-eai/DreamTrue">[3]</a>
  核验：2026-10-12

  </details>

+ [RoboRSI: Stable, efficient, and reusable robot self-evolution in complex real-world environments](<https://arxiv.org/abs/2610.12424>)<br>
  [![Star](https://img.shields.io/github/stars/nssmd/RoboRSI.svg?style=social&label=Star)](<https://github.com/nssmd/RoboRSI>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.12424>) [![Website](https://img.shields.io/badge/Website-9cf.svg)](<https://lab.noematrix.ai/blog/2-roborsi>)
  <br>2026-10-08 · 具身与世界模型

  <details>
  <summary>中文简介：问题 · 方法 · 价值 · 局限</summary>

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
  <summary>中文简介：问题 · 方法 · 价值 · 局限</summary>

  - **问题**：机载导航需评估多个候选路径，但世界模型计算预算有限。
  - **方法**：共享视觉特征编码，用多时域潜在预测评估候选动作轨迹。
  - **价值**：降低重复编码成本，改善实地视觉导航的路径选择。
  - **局限**：真实测试规模较小，嵌入式推理延迟仍限制快速闭环应用。

  来源：<a href="https://arxiv.org/abs/2610.12368">[1]</a>
  核验：2026-10-12

  </details>

+ [PLaW-VLA: Predictive Latent World Modeling for Vision-Language-Action Policies](<https://arxiv.org/abs/2610.12285>)<br>
  [![Star](https://img.shields.io/github/stars/RainyRobo/PLaW-VLA.svg?style=social&label=Star)](<https://github.com/RainyRobo/PLaW-VLA>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.12285>) [![Website](https://img.shields.io/badge/Website-9cf.svg)](<https://rainyrobo.github.io/PLaW-VLA>)
  <br>2026-10-08 · 具身与世界模型

  <details>
  <summary>中文简介：问题 · 方法 · 价值 · 局限</summary>

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
  <summary>中文简介：问题 · 方法 · 价值 · 局限</summary>

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
  <summary>中文简介：问题 · 方法 · 价值 · 局限</summary>

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
  <summary>中文简介：问题 · 方法 · 价值 · 局限</summary>

  - **问题**：像素世界模型规划成本高，潜空间模型的规模收益尚待检验。
  - **方法**：扩展机器人潜在预测模型，以目标图像引导闭环动作规划。
  - **价值**：展示大规模潜空间预测用于控制的潜力并优化规划计算。
  - **局限**：多步规划仍有明显延迟，不能直接视为实时控制方案。

  来源：<a href="https://arxiv.org/abs/2610.10515">[1]</a>
  核验：2026-10-12

  </details>

+ [DepthWorld: 3D World Model for Robot Manipulation](<https://arxiv.org/abs/2610.08780>)<br>
  [![Star](https://img.shields.io/github/stars/Jai2500/depthworld.svg?style=social&label=Star)](<https://github.com/Jai2500/depthworld>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.08780>) [![Website](https://img.shields.io/badge/Website-9cf.svg)](<https://jaibardhan.com/depthworld>) [![Weights](https://img.shields.io/badge/Weights-yellow.svg)](<https://huggingface.co/jaibrdhn/depthworld>)
  <br>2026-10-06 · 具身与世界模型

  <details>
  <summary>中文简介：问题 · 方法 · 价值 · 局限</summary>

  - **问题**：机器人视频世界模型容易产生跨视角不一致的三维几何。
  - **方法**：重新校准多视角数据，联合预测动作条件下的彩色图像与深度。
  - **价值**：改善空间一致性，开放模型权重与标定资源供复现。
  - **局限**：预测质量提升尚不等于策略控制收益，部分数据需申请访问。

  来源：<a href="https://arxiv.org/abs/2610.08780">[1]</a> · <a href="https://github.com/Jai2500/depthworld">[2]</a> · <a href="https://huggingface.co/jaibrdhn/depthworld">[3]</a> · <a href="https://jaibardhan.com/depthworld">[4]</a>
  核验：2026-10-12

  </details>

+ [OpenWAM: An Open Framework for Composable World-Action Models](<https://arxiv.org/abs/2610.07922>)<br>
  [![Star](https://img.shields.io/github/stars/OpenWAM/OpenWAM.svg?style=social&label=Star)](<https://github.com/OpenWAM/OpenWAM>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.07922>) [![Website](https://img.shields.io/badge/Website-9cf.svg)](<https://openwam.stanford.edu/>) [![Weights](https://img.shields.io/badge/Weights-yellow.svg)](<https://huggingface.co/OpenWAM-Stanford/OpenWAM-Pretraining>)
  <br>2026-10-06 · 具身与世界模型

  <details>
  <summary>中文简介：问题 · 方法 · 价值 · 局限</summary>

  - **问题**：世界模型与动作策略常各自训练，组件难以跨任务组合复用。
  - **方法**：共享因果视频骨干，比较视频动作生成顺序并组合正逆动力学。
  - **价值**：提供统一框架和反事实数据训练路径，便于研究组件复用。
  - **局限**：数据量差异影响归因，仿真复用不等于真实机器人零样本迁移。

  来源：<a href="https://arxiv.org/abs/2610.07922">[1]</a> · <a href="https://github.com/OpenWAM/OpenWAM">[2]</a> · <a href="https://huggingface.co/OpenWAM-Stanford/OpenWAM-Pretraining">[3]</a> · <a href="https://openwam.stanford.edu/">[4]</a>
  核验：2026-10-12

  </details>

+ [PointWAM: 3D World Action Modeling for Dexterous Robotic Manipulation](<https://arxiv.org/abs/2610.02840>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.02840>) [![Website](https://img.shields.io/badge/Website-9cf.svg)](<https://chrockey.github.io/PointWAM>)
  <br>2026-10-02 · 具身与世界模型

  <details>
  <summary>中文简介：问题 · 方法 · 价值 · 局限</summary>

  - **问题**：灵巧操作需要理解三维场景变化，单纯动作模仿难以迁移。
  - **方法**：联合预测场景点与手部关键点，再将动作重定向到机器人。
  - **价值**：利用人类视频预训练和三维监督连接世界预测与操作。
  - **局限**：依赖重定向及场景准备，精细接触任务的成功率仍有限。

  来源：<a href="https://arxiv.org/abs/2610.02840">[1]</a> · <a href="https://chrockey.github.io/PointWAM">[2]</a>
  核验：2026-10-12

  </details>


## 交互 Avatar

+ [PixReenact: Pixel-Conditioned Causal Video Diffusion for Streaming Head-Avatar Reenactment](<https://arxiv.org/abs/2610.05233>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.05233>) [![Website](https://img.shields.io/badge/Website-9cf.svg)](<https://gavriel-habib.github.io/pixreenact>)
  <br>2026-10-04 · 交互 Avatar

  <details>
  <summary>中文简介：问题 · 方法 · 价值 · 局限</summary>

  - **问题**：流式头像重演需同时维持身份和跟随驱动视频的头部运动。
  - **方法**：采用像素条件因果扩散、跨身份伪监督及双教师蒸馏。
  - **价值**：以少步分块生成支持低延迟头部头像重演。
  - **局限**：研究范围主要是头部，不等于全身控制或对话交互。

  来源：<a href="https://arxiv.org/abs/2610.05233">[1]</a> · <a href="https://gavriel-habib.github.io/pixreenact">[2]</a>
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

数据和源码公开；不收录 PDF、私人笔记、实验记录或会话原文。推送到 main 后自动验证并部署在线阅读页及离线 ZIP。云端研究任务的接入状态见 [接入说明](docs/INTEGRATION.md)。

组织形式参考 [Awesome-Video-Diffusion](https://github.com/showlab/Awesome-Video-Diffusion)。摘要为本项目独立撰写；论文、模型和源码的使用条件以各原始发布方为准。

# Research Paper Watch

公开论文精选：视频、三维与具身、智能体、多模态检索、评测及训练推理。每篇附可折叠中文简介与一手来源。

**124 篇论文** · [在线阅读（支持快捷键）](https://ripemangobox.github.io/research-paper-watch/) · [下载离线阅读器 ZIP](https://ripemangobox.github.io/research-paper-watch/research-paper-watch.zip) · [唯一数据源](data/papers.json) · [导入与任务接入](docs/INTEGRATION.md)
研究目标：视频生成核心难题、实时交互 Avatar、世界模型、Agent 规划与记忆。会议与期刊按已核实来源标注，无法确认时显示录用待核实。

阅读优先级依据视频生成核心难题、实时交互 Avatar、世界模型、Agent 规划与记忆：**P0 必读 → P1 重点 → P2 选读 → P3 暂缓**。这是课题相关性排序，不是论文质量排名。每篇说明推荐理由；常规阅读范围为 abs + intro。


在线阅读页直接支持搜索、分类、E 全部展开、C 全部收起。离线 ZIP 解压后双击 index.html，无需安装或启动服务器。GitHub README 不运行自定义脚本：可点击简介，或 Tab 聚焦后按 Enter / 空格展开收起；E / C 请使用在线阅读页。

日期为论文首次公开日期；空链接表示尚未核实。简介中的局限包含基于公开证据的阅读边界，不代表作者自述的缺陷。

## 目录

- [视频生成基础](#视频生成基础) · 9
- [少步蒸馏](#少步蒸馏) · 4
- [交互长视频](#交互长视频) · 9
- [流式系统](#流式系统) · 2
- [具身与世界模型](#具身与世界模型) · 14
- [交互 Avatar](#交互-avatar) · 4
- [智能体与上下文](#智能体与上下文) · 20
- [多模态检索](#多模态检索) · 6
- [评测与可靠性](#评测与可靠性) · 20
- [训练与推理效率](#训练与推理效率) · 14
- [多模态架构与综述](#多模态架构与综述) · 5
- [三维生成与重建](#三维生成与重建) · 3
- [图像生成与编辑](#图像生成与编辑) · 2
- [视频理解与推理](#视频理解与推理) · 1
- [语音与音频](#语音与音频) · 2
- [视觉感知](#视觉感知) · 3
- [领域应用](#领域应用) · 6

## 视频生成基础

+ [Connected Self Forcing: Beyond Local Learning in Video Autoregression](<https://arxiv.org/abs/2610.12156>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.12156>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://eastbeanzhang.github.io/CSF>)
  <br>2026-10-08 · 梯度回放 / 自回归扩散 / 误差累积 / 长视频

  **arXiv 预印本（录用待核实）** · **P0 必读** · 摘要与引言
  跨片段梯度与长时信用分配直接触及自回归视频漂移的训练根源。

  <details>
  <summary>brief</summary>

  - **问题**：局部自回归训练截断历史梯度，早期生成难获后续误差信号。
  - **方法**：使用快捷梯度重放连接历史潜变量及注意力缓存。
  - **价值**：在不增加推理开销的情况下改善长视频训练与稳定性。
  - **局限**：训练需要额外重放成本，长时稳定与运动丰富度仍需权衡。

  来源：<a href="https://arxiv.org/abs/2610.12156">[1]</a> · <a href="https://arxiv.org/pdf/2610.12156">[2]</a> · <a href="https://eastbeanzhang.github.io/CSF">[3]</a>
  核验：2026-10-13

  </details>

+ [SGF+: Decoupling Gradient Flows for Autoregressive Video Generation](<https://arxiv.org/abs/2610.10429>)<br>
  [![Star](https://img.shields.io/github/stars/Zihan-Su/Self_Gradient_Forcing_Plus.svg?style=social&label=Star)](<https://github.com/Zihan-Su/Self_Gradient_Forcing_Plus>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.10429>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://zihan-su.github.io/self-gradient-forcing-plus>) [![Weights](https://img.shields.io/badge/Weights-yellow.svg)](<https://huggingface.co/ZihanSu/Self_Gradient_Forcing_Plus>)
  <br>2026-10-07 · 上下文写入 / 梯度冲突 / 自回归扩散 / 长视频

  **arXiv 预印本（录用待核实）** · **P0 必读** · 摘要与引言
  区分写入历史与当前去噪的优化冲突，可与跨片段梯度方法直接比较。

  <details>
  <summary>brief</summary>

  - **问题**：自回归视频中缓存写入与当前去噪的梯度目标可能冲突。
  - **方法**：分离写入器和去噪器参数，再通过因果注意力联合训练。
  - **价值**：提高长时滚动生成的稳定性，提供可复现代码与权重。
  - **局限**：稳定性可能伴随动态程度降低，固定缓存仍有记忆边界。

  来源：<a href="https://arxiv.org/abs/2610.10429">[1]</a> · <a href="https://arxiv.org/pdf/2610.10429">[2]</a> · <a href="https://github.com/Zihan-Su/Self_Gradient_Forcing_Plus">[3]</a> · <a href="https://huggingface.co/ZihanSu/Self_Gradient_Forcing_Plus">[4]</a> · <a href="https://zihan-su.github.io/self-gradient-forcing-plus">[5]</a>
  核验：2026-10-13

  </details>

+ [SoliReward: Mitigating Susceptibility to Reward Hacking and Annotation Noise in Video Generation Reward Models](<https://arxiv.org/abs/2512.22170>)<br>
  [![Star](https://img.shields.io/github/stars/lian700/SoliReward.svg?style=social&label=Star)](<https://github.com/lian700/SoliReward>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2512.22170>)
  <br>2025-12-17 · 奖励模型 / 强化学习 / 物理合理性 / 视频生成

  **[CVPR 2026](<https://openaccess.thecvf.com/content/CVPR2026/html/Lian_SoliReward_Mitigating_Susceptibility_to_Reward_Hacking_and_Annotation_Noise_in_CVPR_2026_paper.html>)** · **P0 必读** · 摘要与引言
  直接处理视频后训练的奖励可靠性和物理缺陷，优先精读。

  <details>
  <summary>brief</summary>

  - **问题**：成对偏好噪声与奖励尖峰会误导视频后训练，单层输出也难兼顾多种缺陷。
  - **方法**：以单项二元标注跨提示配对，结合分层特征聚合及允许平局的排序损失。
  - **价值**：改善物理、畸变和语义评价并缓解奖励投机。
  - **局限**：二元质量维度与代理奖励仍有限，不能保证开放场景物理正确。

  来源：<a href="https://arxiv.org/abs/2512.22170">[1]</a> · <a href="https://arxiv.org/pdf/2512.22170">[2]</a> · <a href="https://github.com/lian700/SoliReward">[3]</a> · <a href="https://openaccess.thecvf.com/content/CVPR2026/html/Lian_SoliReward_Mitigating_Susceptibility_to_Reward_Hacking_and_Annotation_Noise_in_CVPR_2026_paper.html">[4]</a>
  核验：2026-10-13

  </details>

+ [Harmony: Harmonizing Audio and Video Generation through Cross-Task Synergy](<https://arxiv.org/abs/2511.21579>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2511.21579>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://sjtuplayer.github.io/projects/Harmony>)
  <br>2025-11-26 · Avatar / 跨模态同步 / 音视频生成

  **[CVPR 2026](<https://openaccess.thecvf.com/content/CVPR2026/html/Hu_Harmony_Harmonizing_Audio_and_Video_Generation_through_Cross-Task_Synergy_CVPR_2026_paper.html>)** · **P0 必读** · 摘要与引言
  与 UniAVGen 对读，聚焦联合去噪时音画同步的机制。

  <details>
  <summary>brief</summary>

  - **问题**：两种模态同时从噪声演化，映射关系漂移且局部同步与全局风格相互牵制。
  - **方法**：联合条件任务训练，拆分全局局部交互，并单独增强同步指导信号。
  - **价值**：兼顾语音、环境音与视频的一致生成。
  - **局限**：质量提升主要面向离线合成，尚不能据此认定支持实时可打断交互。

  来源：<a href="https://arxiv.org/abs/2511.21579">[1]</a> · <a href="https://arxiv.org/pdf/2511.21579">[2]</a> · <a href="https://openaccess.thecvf.com/content/CVPR2026/html/Hu_Harmony_Harmonizing_Audio_and_Video_Generation_through_Cross-Task_Synergy_CVPR_2026_paper.html">[3]</a> · <a href="https://sjtuplayer.github.io/projects/Harmony">[4]</a>
  核验：2026-10-13

  </details>

+ [UniAVGen: Unified Audio and Video Generation with Asymmetric Cross-Modal Interactions](<https://arxiv.org/abs/2511.03334>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2511.03334>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://mcg-nju.github.io/UniAVGen>)
  <br>2025-11-05 · Avatar / 跨模态同步 / 音视频生成

  **[CVPR 2026](<https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_UniAVGen_Unified_Audio_and_Video_Generation_with_Asymmetric_Cross-Modal_Interactions_CVPR_2026_paper.html>)** · **P0 必读** · 摘要与引言
  人类音视频联合生成与同步控制直接对应交互 Avatar。

  <details>
  <summary>brief</summary>

  - **问题**：分阶段音视频生成缺乏双向交互，容易出现口型和情绪不一致。
  - **方法**：双扩散分支通过非对称时间对齐注意力交换信息，并强化面部区域和跨模态指导。
  - **价值**：统一联合生成、配音和音频驱动视频。
  - **局限**：联合生成质量不等于流式低延迟，在线打断与轮次响应需另行验证。

  来源：<a href="https://arxiv.org/abs/2511.03334">[1]</a> · <a href="https://arxiv.org/pdf/2511.03334">[2]</a> · <a href="https://mcg-nju.github.io/UniAVGen">[3]</a> · <a href="https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_UniAVGen_Unified_Audio_and_Video_Generation_with_Asymmetric_Cross-Modal_Interactions_CVPR_2026_paper.html">[4]</a>
  核验：2026-10-13

  </details>

+ [Diffusion Forcing: Next-token Prediction Meets Full-Sequence Diffusion](<https://arxiv.org/abs/2407.01392>)<br>
  [![Star](https://img.shields.io/github/stars/buoyancy99/diffusion-forcing.svg?style=social&label=Star)](<https://github.com/buoyancy99/diffusion-forcing>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2407.01392>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://www.boyuan.space/diffusion-forcing>)
  <br>2024-07-01 · 因果建模 / 基础方法 / 扩散强制 / 轨迹规划

  **[NeurIPS 2024](<https://arxiv.org/pdf/2407.01392>)** · **P0 必读** · 摘要与引言
  独立逐词元噪声把可变长预测与轨迹引导结合，是视频世界模型及规划的共同基础。

  <details>
  <summary>brief</summary>

  - **问题**：序列预测的灵活长度与整段扩散的引导能力难以兼得。
  - **方法**：训练时为各个序列元素独立设置噪声等级，以因果模型学习不同噪声组合下的去噪。
  - **价值**：统一变长生成、长时序外推和规划引导，为视频及决策提供通用思路。
  - **局限**：原论文使用循环网络；当前主分支已改为时序注意力，复现需区分版本。

  来源：<a href="https://arxiv.org/abs/2407.01392">[1]</a> · <a href="https://arxiv.org/pdf/2407.01392">[2]</a> · <a href="https://github.com/buoyancy99/diffusion-forcing">[3]</a> · <a href="https://www.boyuan.space/diffusion-forcing">[4]</a>
  核验：2026-10-13

  </details>

+ [Manifold-Optimal Guidance: A Unified Riemannian Control View of Diffusion Guidance](<https://arxiv.org/abs/2603.11509>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2603.11509>)
  <br>2026-03-12 · 可控生成 / 扩散引导 / 采样稳定性

  **[ICML 2026](<https://proceedings.mlr.press/v306/jia26g.html>)** · **P1 重点** · 摘要与引言
  可控生成中强引导引起的质量退化是通用难题，几何视角值得迁移到视频采样。

  <details>
  <summary>brief</summary>

  - **问题**：强分类器自由引导可能把采样推离高密度区域，造成过饱和与结构损坏。
  - **方法**：将引导写成局部黎曼最优控制，以几何度量修正方向并动态平衡引导强度。
  - **价值**：提供无需重训的采样修正思路，连接条件对齐与生成质量。
  - **局限**：实际效果依赖几何近似，不能由图像质量改进推导视频动力学可靠性。

  来源：<a href="https://arxiv.org/abs/2603.11509">[1]</a> · <a href="https://arxiv.org/pdf/2603.11509">[2]</a> · <a href="https://proceedings.mlr.press/v306/jia26g.html">[3]</a>
  核验：2026-10-13

  </details>

+ [Arbitrary Generative Video Interpolation](<https://arxiv.org/abs/2510.00578>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2510.00578>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://mcg-nju.github.io/ArbInterp-Web>)
  <br>2025-10-01 · 时间控制 / 视频插帧 / 运动一致性

  **[ICLR 2026](<https://proceedings.iclr.cc/paper_files/paper/2026/hash/36572cc8bb2a939f0d998847cb44776e-Abstract-Conference.html>)** · **P1 重点** · 摘要与引言
  连续时间控制和跨段运动传递值得用于视频生成，但双端条件不适用于即时未知未来。

  <details>
  <summary>brief</summary>

  - **问题**：生成式插帧通常固定帧数，难按目标时间采样并延长连续过渡。
  - **方法**：用时间戳调节旋转位置编码，分段生成时分别传递前段外观与运动条件。
  - **价值**：把插帧扩展为任意时刻查询，提供时间控制与跨段衔接的简洁设计。
  - **局限**：依赖已知首尾帧，长序列插值不等于无终点的实时交互生成。

  来源：<a href="https://arxiv.org/abs/2510.00578">[1]</a> · <a href="https://arxiv.org/pdf/2510.00578">[2]</a> · <a href="https://mcg-nju.github.io/ArbInterp-Web">[3]</a> · <a href="https://proceedings.iclr.cc/paper_files/paper/2026/hash/36572cc8bb2a939f0d998847cb44776e-Abstract-Conference.html">[4]</a>
  核验：2026-10-13

  </details>

+ [TEMPFLOW-GRPO: WHEN TIMING MATTERS FOR GRPO IN FLOW MODELS](<https://arxiv.org/abs/2508.04324>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2508.04324>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://tempflowgrpo.github.io/>)
  <br>2025-08-06 · 信用分配 / 流匹配 / 生成后训练

  **[ICLR 2026](<https://proceedings.iclr.cc/paper_files/paper/2026/hash/d75f561eaaf2cb754bc8d7e36d8af362-Abstract-Conference.html>)** · **P1 重点** · 摘要与引言
  生成模型后训练的去噪步信用分配值得与 WorldCompass 的片段级奖励对照。

  <details>
  <summary>brief</summary>

  - **问题**：流模型各去噪阶段作用不同，统一使用终局奖励会浪费关键阶段的探索。
  - **方法**：仅在指定步骤分叉随机轨迹，按噪声加权更新，并控制初始种子隔离探索贡献。
  - **价值**：无需中间奖励模型即可估计步骤贡献，为生成过程优化提供工具。
  - **局限**：这里的时间指去噪进程而非视频帧序，迁移到长视频需要重新设计评价。

  来源：<a href="https://arxiv.org/abs/2508.04324">[1]</a> · <a href="https://arxiv.org/pdf/2508.04324">[2]</a> · <a href="https://proceedings.iclr.cc/paper_files/paper/2026/hash/d75f561eaaf2cb754bc8d7e36d8af362-Abstract-Conference.html">[3]</a> · <a href="https://tempflowgrpo.github.io/">[4]</a>
  核验：2026-10-13

  </details>


## 少步蒸馏

+ [Causal Forcing: Autoregressive Diffusion Distillation Done Right for High-Quality Real-Time Interactive Video Generation](<https://arxiv.org/abs/2602.02214>)<br>
  [![Star](https://img.shields.io/github/stars/thu-ml/Causal-Forcing.svg?style=social&label=Star)](<https://github.com/thu-ml/Causal-Forcing>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2602.02214>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://thu-ml.github.io/CausalForcing.github.io>) [![Weights](https://img.shields.io/badge/Weights-yellow.svg)](<https://huggingface.co/zhuhz22/Causal-Forcing/tree/main>)
  <br>2026-02-02 · ODE初始化 / 因果蒸馏 / 实时视频 / 理论分析

  **[ICML 2026](<https://arxiv.org/abs/2602.02214>)** · **P0 必读** · 摘要与引言
  从帧级单射性分析双向教师到因果学生的初始化失配，是实时视频蒸馏的核心阅读。

  <details>
  <summary>brief</summary>

  - **问题**：双向教师的轨迹初始化与因果学生存在结构不匹配。
  - **方法**：先训练自回归教师，再用因果常微分方程轨迹初始化少步学生，随后进行非对称分布匹配蒸馏。
  - **价值**：改善蒸馏起点，在既定实验设置中提高视频质量与运动表现。
  - **局限**：本条针对原始三阶段方法；后续增强版另有一致性蒸馏，不能混用其结论。

  来源：<a href="https://arxiv.org/abs/2602.02214">[1]</a> · <a href="https://arxiv.org/pdf/2602.02214">[2]</a> · <a href="https://github.com/thu-ml/Causal-Forcing">[3]</a> · <a href="https://huggingface.co/zhuhz22/Causal-Forcing/tree/main">[4]</a> · <a href="https://thu-ml.github.io/CausalForcing.github.io">[5]</a>
  核验：2026-10-13

  </details>

+ [Self Forcing: Bridging the Train-Test Gap in Autoregressive Video Diffusion](<https://arxiv.org/abs/2506.08009>)<br>
  [![Star](https://img.shields.io/github/stars/guandeh17/Self-Forcing.svg?style=social&label=Star)](<https://github.com/guandeh17/Self-Forcing>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2506.08009>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://self-forcing.github.io/>) [![Weights](https://img.shields.io/badge/Weights-yellow.svg)](<https://huggingface.co/gdhe17/Self-Forcing/tree/main>)
  <br>2025-06-09 · 实时视频 / 暴露偏差 / 自回归扩散 / 自生成训练

  **[NeurIPS 2025 Spotlight](<https://arxiv.org/abs/2506.08009>)** · **P0 必读** · 摘要与引言
  用自生成历史训练直接处理暴露偏差，是理解后续长视频 forcing 方法的基础。

  <details>
  <summary>brief</summary>

  - **问题**：真实历史训练与模型生成历史推理之间的偏差会累积。
  - **方法**：训练中直接自回归展开并缓存自生成历史，用整段视频损失监督，配合少步去噪与随机梯度截断。
  - **价值**：将训练条件贴近部署过程，支持低延迟流式视频生成。
  - **局限**：演示依赖指定硬件与模型设置；长而详细的提示词效果更好，不能外推所有场景。

  来源：<a href="https://arxiv.org/abs/2506.08009">[1]</a> · <a href="https://arxiv.org/pdf/2506.08009">[2]</a> · <a href="https://github.com/guandeh17/Self-Forcing">[3]</a> · <a href="https://huggingface.co/gdhe17/Self-Forcing/tree/main">[4]</a> · <a href="https://self-forcing.github.io/">[5]</a>
  核验：2026-10-13

  </details>

+ [From Slow Bidirectional to Fast Autoregressive Video Diffusion Models](<https://arxiv.org/abs/2412.07772>)<br>
  [![Star](https://img.shields.io/github/stars/tianweiy/CausVid.svg?style=social&label=Star)](<https://github.com/tianweiy/CausVid>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2412.07772>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://causvid.github.io/>) [![Weights](https://img.shields.io/badge/Weights-yellow.svg)](<https://huggingface.co/tianweiy/CausVid/tree/main/autoregressive_checkpoint>)
  <br>2024-12-10 · KV缓存 / 分布匹配蒸馏 / 因果视频 / 基础方法

  **[CVPR 2025](<https://arxiv.org/abs/2412.07772>)** · **P0 必读** · 摘要与引言
  双向教师到因果少步学生的蒸馏建立实时视频路线，宜先于各类 forcing 改进阅读。

  <details>
  <summary>brief</summary>

  - **问题**：双向视频扩散依赖未来帧，难以低延迟逐帧生成。
  - **方法**：通过教师轨迹初始化、非对称分布匹配蒸馏及因果注意力，将多步模型转为少步自回归生成器。
  - **价值**：结合缓存支持流式生成，并展示动态提示与长视频能力。
  - **局限**：少步生成仍依赖教师质量；公开仓库的示例训练不等同于论文全部实验。

  来源：<a href="https://arxiv.org/abs/2412.07772">[1]</a> · <a href="https://arxiv.org/pdf/2412.07772">[2]</a> · <a href="https://causvid.github.io/">[3]</a> · <a href="https://github.com/tianweiy/CausVid">[4]</a> · <a href="https://huggingface.co/tianweiy/CausVid/tree/main/autoregressive_checkpoint">[5]</a>
  核验：2026-10-13

  </details>

+ [VideoLCM: Video Latent Consistency Model](<https://arxiv.org/abs/2312.09109>)<br>
  [![Star](https://img.shields.io/github/stars/ali-vilab/VGen.svg?style=social&label=Star)](<https://github.com/ali-vilab/VGen>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2312.09109>)
  <br>2023-12-14 · 一致性蒸馏 / 少步生成 / 视频扩散

  **arXiv 预印本（录用待核实）** · **P1 重点** · 摘要与引言
  视频潜在一致性蒸馏的早期基线，帮助理解少步生成，但本身不解决因果交互。

  <details>
  <summary>brief</summary>

  - **问题**：视频扩散多步采样成本高。
  - **方法**：在潜空间用冻结教师的DDIM轨迹配对和EMA学生目标做一致性蒸馏。
  - **价值**：复用预训练模型，将文生视频压缩至约4–6步，并支持组合条件生成。
  - **局限**：依赖强教师与匹配数据，仍需微调，论文尚未实现实时生成。

  来源：<a href="https://arxiv.org/abs/2312.09109">[1]</a> · <a href="https://arxiv.org/html/2312.09109">[2]</a> · <a href="https://arxiv.org/pdf/2312.09109">[3]</a> · <a href="https://github.com/ali-vilab/VGen">[4]</a>
  核验：2026-10-13

  </details>


## 交互长视频

+ [Memory Forcing: Attendable Mid-Horizon History for Streaming Video Generation](<https://arxiv.org/abs/2610.11756>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.11756>)
  <br>2026-10-08 · KV缓存 / 流式生成 / 视频记忆 / 长时一致性

  **arXiv 预印本（录用待核实）** · **P0 必读** · 摘要与引言
  固定预算下保存中程事件并重新编码时间，正面解决流式视频的离开再返回遗忘。

  <details>
  <summary>brief</summary>

  - **问题**：流式视频滑动窗口会丢失中期历史，使早先内容难以延续。
  - **方法**：划分锚点、档案和工作缓存，结合历史选择与分库位置编码。
  - **价值**：在固定缓存预算下增加可访问历史并改善连续性。
  - **局限**：尚非语义检索或持久世界状态，视频帧率不代表生成速度。

  来源：<a href="https://arxiv.org/abs/2610.11756">[1]</a> · <a href="https://arxiv.org/pdf/2610.11756">[2]</a>
  核验：2026-10-13

  </details>

+ [Keepsake: Selective Spatial Memory for Long-Horizon Video Generation](<https://arxiv.org/abs/2610.06588>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.06588>)
  <br>2026-10-05 · 空间记忆 / 选择性遗忘 / 长时一致性

  **arXiv 预印本（录用待核实）** · **P0 必读** · 摘要与引言
  研究有限空间记忆如何持续淘汰冗余视角，直接对应长时世界模型的记忆预算。

  <details>
  <summary>brief</summary>

  - **问题**：长视频空间记忆随历史增长而膨胀，重复视角挤占有限缓存。
  - **方法**：用姿态与外观图选择固定容量记忆，淘汰可被替代的观测。
  - **价值**：无需重训生成器即可改善长时间空间一致性。
  - **局限**：测试轨迹规模有限，尚不能保证动态场景状态正确。

  来源：<a href="https://arxiv.org/abs/2610.06588">[1]</a> · <a href="https://arxiv.org/pdf/2610.06588">[2]</a>
  核验：2026-10-13

  </details>

+ [LoGo: Local-Global Rewards for Consistent Long-Horizon Video Generation](<https://arxiv.org/abs/2610.03636>)<br>
  [![Star](https://img.shields.io/github/stars/ziqi-ma/logo.svg?style=social&label=Star)](<https://github.com/ziqi-ma/logo>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.03636>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://ziqi-ma.github.io/logo-website>) [![Weights](https://img.shields.io/badge/Weights-yellow.svg)](<https://huggingface.co/ziqima/LoGo>)
  <br>2026-10-02 · 三维一致性 / 世界模型 / 局部奖励 / 生成后训练

  **arXiv 预印本（录用待核实）** · **P0 必读** · 摘要与引言
  局部几何奖励补足全局美学评分的盲点，适合研究世界模型的三维一致性后训练。

  <details>
  <summary>brief</summary>

  - **问题**：长时视频的局部画面质量与全局三维一致性往往难以兼顾。
  - **方法**：组合局部与全局几何奖励，对视频生成模型进行后训练。
  - **价值**：改善相机运动下场景一致性，并发布训练代码与适配器。
  - **局限**：证据主要来自静态场景，不能外推至动态人体或复杂交互。

  来源：<a href="https://arxiv.org/abs/2610.03636">[1]</a> · <a href="https://arxiv.org/pdf/2610.03636">[2]</a> · <a href="https://github.com/ziqi-ma/logo">[3]</a> · <a href="https://huggingface.co/ziqima/LoGo">[4]</a> · <a href="https://ziqi-ma.github.io/logo-website">[5]</a>
  核验：2026-10-13

  </details>

+ [Weave Forcing: Compositional Memory Routing for Interactive Long Video Generation](<https://arxiv.org/abs/2610.03510>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.03510>)
  <br>2026-10-02 · 交互视频 / 组合记忆 / 语义路由 / 跨镜头一致性

  **arXiv 预印本（录用待核实）** · **P0 必读** · 摘要与引言
  语义槽检索和局部 KV 掩码把历史主体与场景重新组合，连接视频记忆与交互规划。

  <details>
  <summary>brief</summary>

  - **问题**：交互长视频需要重组历史人物与背景，单一记忆难以匹配。
  - **方法**：以语义槽和区域掩码路由历史缓存，并自适应调整位置编码。
  - **价值**：支持跨镜头组合记忆，增强人物与场景延续性。
  - **局限**：端到端实时性与复杂动态交互仍缺充分验证。

  来源：<a href="https://arxiv.org/abs/2610.03510">[1]</a> · <a href="https://arxiv.org/pdf/2610.03510">[2]</a>
  核验：2026-10-13

  </details>

+ [MosaiChunk: Compositing Spatio-Temporal Memory for Autoregressive Video Generation](<https://arxiv.org/abs/2610.02153>)<br>
  [![Star](https://img.shields.io/github/stars/mosaichunk/MosaiChunk.svg?style=social&label=Star)](<https://github.com/mosaichunk/MosaiChunk>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.02153>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://mosaichunk.github.io/>) [![Weights](https://img.shields.io/badge/Weights-yellow.svg)](<https://huggingface.co/mosaichunk/MosaiChunk>)
  <br>2026-10-01 · KV检索 / 组合记忆 / 自蒸馏 / 重访一致性

  **arXiv 预印本（录用待核实）** · **P0 必读** · 摘要与引言
  固定预算下重组历史 KV 区域并蒸馏检索器，直接针对遮挡后重现和长视频遗忘。

  <details>
  <summary>brief</summary>

  - **问题**：自回归视频有限缓存难以记住离开视野后再次出现的场景。
  - **方法**：冻结生成器，训练轻量路由器组合历史时空片段的注意力缓存。
  - **价值**：在固定活动缓存下增强重访一致性，支持长时记忆检索。
  - **局限**：主机历史存储仍会增长，旧记忆与动态状态冲突尚未解决。

  来源：<a href="https://arxiv.org/abs/2610.02153">[1]</a> · <a href="https://arxiv.org/pdf/2610.02153">[2]</a> · <a href="https://github.com/mosaichunk/MosaiChunk">[3]</a> · <a href="https://huggingface.co/mosaichunk/MosaiChunk">[4]</a> · <a href="https://mosaichunk.github.io/">[5]</a>
  核验：2026-10-13

  </details>

+ [ShotVerse: Advancing Cinematic Camera Control for Text-Driven Multi-Shot Video Creation](<https://arxiv.org/abs/2603.11421>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2603.11421>)
  <br>2026-03-12 · 多镜头生成 / 相机控制 / 规划执行 / 视频Agent

  **[SIGGRAPH Asia 2026](<https://arxiv.org/abs/2603.11421>)** · **P0 必读** · 已核对正文
  显式相机轨迹连接叙事规划与生成执行，是视频控制与 Agent 规划交叉的直接案例。

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
  <br>2026-02-05 · 少步扩散 / 测试时校正 / 误差累积 / 长视频

  **[ECCV 2026](<https://cs.nju.edu.cn/rl/papers.htm>)** · **P0 必读** · 已核对正文
  无需训练的采样路径校正直接针对少步长视频漂移，适合与训练式补救作对照。

  <details>
  <summary>brief</summary>

  - **问题**：少步自回归视频累积漂移，测试时梯度优化又易破坏蒸馏模型。
  - **方法**：待全局结构稳定后，以首帧条件校正中间预测，再加噪回当前时间步的方差水平。
  - **价值**：无需重训即可干预采样轨迹，作者报告改善30秒生成稳定性。
  - **局限**：依赖初始锚点与随机采样过程；额外校正仍有推理开销。

  来源：<a href="https://arxiv.org/abs/2602.05871">[1]</a> · <a href="https://arxiv.org/pdf/2602.05871v2">[2]</a> · <a href="https://cs.nju.edu.cn/rl/papers.htm">[3]</a> · <a href="https://ttc-1231.github.io/">[4]</a>
  核验：2026-10-13

  </details>

+ [Rolling Forcing: Autoregressive Long Video Diffusion in Real Time](<https://arxiv.org/abs/2509.25161>)<br>
  [![Star](https://img.shields.io/github/stars/TencentARC/RollingForcing.svg?style=social&label=Star)](<https://github.com/TencentARC/RollingForcing>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2509.25161>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://kunhao-liu.github.io/Rolling_Forcing_Webpage>) [![Weights](https://img.shields.io/badge/Weights-yellow.svg)](<https://huggingface.co/TencentARC/RollingForcing>)
  <br>2025-09-29 · 滚动生成 / 自回归扩散 / 误差累积 / 长视频

  **[ICLR 2026](<https://proceedings.iclr.cc/paper_files/paper/2026/hash/935151cc6cb5d8b6816133b75233775a-Abstract-Conference.html>)** · **P0 必读** · 摘要与引言
  滚动噪声块和自生成上下文训练共同处理长视频误差累积，是交互生成的重要基线。

  <details>
  <summary>brief</summary>

  - **问题**：逐帧生成的误差容易在长视频中持续传播。
  - **方法**：在滚动窗口内联合去噪不同噪声等级的帧，保留初始帧缓存作全局锚点，并以非重叠窗口训练。
  - **价值**：在控制训练成本的同时改善长时一致性，展示分钟级实时流式视频。
  - **局限**：联合窗口放宽了相邻帧严格因果性；长视频展示不等于对任意时长的稳定保证。

  来源：<a href="https://arxiv.org/abs/2509.25161">[1]</a> · <a href="https://arxiv.org/pdf/2509.25161">[2]</a> · <a href="https://github.com/TencentARC/RollingForcing">[3]</a> · <a href="https://huggingface.co/TencentARC/RollingForcing">[4]</a> · <a href="https://kunhao-liu.github.io/Rolling_Forcing_Webpage">[5]</a> · <a href="https://proceedings.iclr.cc/paper_files/paper/2026/hash/935151cc6cb5d8b6816133b75233775a-Abstract-Conference.html">[6]</a>
  核验：2026-10-13

  </details>

+ [LongLive: Real-time Interactive Long Video Generation](<https://arxiv.org/abs/2509.22622>)<br>
  [![Star](https://img.shields.io/github/stars/NVlabs/LongLive.svg?style=social&label=Star)](<https://github.com/NVlabs/LongLive>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2509.22622>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://nvlabs.github.io/LongLive>) [![Weights](https://img.shields.io/badge/Weights-yellow.svg)](<https://huggingface.co/Efficient-Large-Model/LongLive-1.3B>)
  <br>2025-09-26 · KV缓存 / 交互长视频 / 提示切换 / 流式训练

  **[ICLR 2026](<https://proceedings.iclr.cc/paper_files/paper/2026/hash/91a1610c6ed9e02d33f826b46f472b92-Abstract-Conference.html>)** · **P0 必读** · 摘要与引言
  长训练、提示切换和 KV 重缓存共同支持持续交互，是实时长视频的关键系统基线。

  <details>
  <summary>brief</summary>

  - **问题**：长视频既要保持一致性，也要及时响应用户提示变化。
  - **方法**：用提示切换时的缓存重算、流式长时训练，以及短窗口注意力和帧锚点维持生成状态。
  - **价值**：将短片模型扩展到可交互的分钟级生成，兼顾响应速度与持续叙事。
  - **局限**：本条对应原始一代论文；速度与时长取决于硬件和配置，不代表任意设备表现。

  来源：<a href="https://arxiv.org/abs/2509.22622">[1]</a> · <a href="https://arxiv.org/pdf/2509.22622">[2]</a> · <a href="https://github.com/NVlabs/LongLive">[3]</a> · <a href="https://huggingface.co/Efficient-Large-Model/LongLive-1.3B">[4]</a> · <a href="https://nvlabs.github.io/LongLive">[5]</a> · <a href="https://proceedings.iclr.cc/paper_files/paper/2026/hash/91a1610c6ed9e02d33f826b46f472b92-Abstract-Conference.html">[6]</a>
  核验：2026-10-13

  </details>


## 流式系统

+ [Real-Time Joint Audio-Video Generation by Parallel Adapter Composition](<https://arxiv.org/abs/2610.10343>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.10343>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://pac-demo-2027.github.io/demo>)
  <br>2026-10-07 · 实时生成 / 蒸馏 / 适配器组合 / 音视频生成

  **arXiv 预印本（录用待核实）** · **P0 必读** · 摘要与引言
  因果化与少步生成适配器的可组合性，直接服务实时音视频 Avatar 的低成本改造。

  <details>
  <summary>brief</summary>

  - **问题**：联合音视频生成难以同时获得跨模态同步与少步推理。
  - **方法**：冻结主干，将因果音视频适配器与少步适配器并行组合。
  - **价值**：减少联合重训需求，展示流式音视频生成能力。
  - **局限**：吞吐依赖多卡，首帧延迟和口型漂移仍影响交互体验。

  来源：<a href="https://arxiv.org/abs/2610.10343">[1]</a> · <a href="https://arxiv.org/pdf/2610.10343">[2]</a> · <a href="https://pac-demo-2027.github.io/demo">[3]</a>
  核验：2026-10-13

  </details>

+ [StreamDiffusionV2: A Streaming System for Dynamic and Interactive Video Generation](<https://arxiv.org/abs/2511.07399>)<br>
  [![Star](https://img.shields.io/github/stars/chenfengxu714/StreamDiffusionV2.svg?style=social&label=Star)](<https://github.com/chenfengxu714/StreamDiffusionV2>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2511.07399>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://streamdiffusionv2.github.io/>) [![Weights](https://img.shields.io/badge/Weights-yellow.svg)](<https://huggingface.co/jerryfeng/StreamDiffusionV2>)
  <br>2025-11-10 · 实时生成 / 服务调度 / 流式系统 / 首帧延迟

  **[MLSys 2026](<https://arxiv.org/abs/2511.07399>)** · **P0 必读** · 摘要与引言
  明确首帧延迟、逐帧截止时间和多卡调度，直接服务实时交互 Avatar 落地。

  <details>
  <summary>brief</summary>

  - **问题**：离线吞吐优化难以满足直播首帧延迟与逐帧截止时间。
  - **方法**：通过延迟目标感知调度、滚动缓存与跨去噪步骤和网络层的流水线组织视频扩散推理。
  - **价值**：无需额外训练即可支持交互视频流和多卡扩展，连接模型与实时服务。
  - **局限**：高帧率报告有特定多卡条件；系统加速不等于底层模型生成能力提升。

  来源：<a href="https://arxiv.org/abs/2511.07399">[1]</a> · <a href="https://arxiv.org/pdf/2511.07399">[2]</a> · <a href="https://github.com/chenfengxu714/StreamDiffusionV2">[3]</a> · <a href="https://huggingface.co/jerryfeng/StreamDiffusionV2">[4]</a> · <a href="https://streamdiffusionv2.github.io/">[5]</a>
  核验：2026-10-13

  </details>


## 具身与世界模型

+ [DreamTrue: Action-Faithful Robot World Model with Counterfactual Post-Training](<https://arxiv.org/abs/2610.12468>)<br>
  [![Star](https://img.shields.io/github/stars/brave-eai/DreamTrue.svg?style=social&label=Star)](<https://github.com/brave-eai/DreamTrue>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.12468>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://brave-eai.github.io/DreamTrue>)
  <br>2026-10-08 · 世界模型 / 动作控制 / 反事实训练 / 物理一致性

  **arXiv 预印本（录用待核实）** · **P0 必读** · 摘要与引言
  反事实动作与缺陷奖励直接针对世界模型的动作忠实度和成功偏差。

  <details>
  <summary>brief</summary>

  - **问题**：机器人世界模型可能生成视觉合理却不忠实于输入动作的结果。
  - **方法**：结合多视角几何校准、缺陷奖励及反事实强化后训练。
  - **价值**：提高动作条件预测的忠实度，减少违背控制指令的幻觉。
  - **局限**：当前主要验证预测质量，尚不能直接推断实际策略成功率提升。

  来源：<a href="https://arxiv.org/abs/2610.12468">[1]</a> · <a href="https://arxiv.org/pdf/2610.12468">[2]</a> · <a href="https://brave-eai.github.io/DreamTrue">[3]</a> · <a href="https://github.com/brave-eai/DreamTrue">[4]</a>
  核验：2026-10-13

  </details>

+ [RoboRSI: Stable, efficient, and reusable robot self-evolution in complex real-world environments](<https://arxiv.org/abs/2610.12424>)<br>
  [![Star](https://img.shields.io/github/stars/nssmd/RoboRSI.svg?style=social&label=Star)](<https://github.com/nssmd/RoboRSI>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.12424>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://lab.noematrix.ai/blog/2-roborsi>)
  <br>2026-10-08 · Agent规划 / 技能记忆 / 自我改进

  **arXiv 预印本（录用待核实）** · **P0 必读** · 摘要与引言
  技能树、执行归因与验证后复用直接连接 Agent 规划和程序性记忆。

  <details>
  <summary>brief</summary>

  - **问题**：复杂真实环境中的机器人需从失败中修正程序并复用经验。
  - **方法**：通过执行反馈迭代代码与技能，在连续任务中积累可用方案。
  - **价值**：展示真实机器人自我改进系统的工程路径和案例。
  - **局限**：运行期间持续开发且存在人工协助，不能视作冻结策略的自主性评测。

  来源：<a href="https://arxiv.org/abs/2610.12424">[1]</a> · <a href="https://arxiv.org/pdf/2610.12424">[2]</a> · <a href="https://github.com/nssmd/RoboRSI">[3]</a> · <a href="https://lab.noematrix.ai/blog/2-roborsi">[4]</a>
  核验：2026-10-13

  </details>

+ [LiteNWM: Efficient Latent World Models for Onboard Visual Navigation in the Wild](<https://arxiv.org/abs/2610.12368>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.12368>)
  <br>2026-10-08 · 潜空间世界模型 / 规划 / 高效推理

  **arXiv 预印本（录用待核实）** · **P0 必读** · 摘要与引言
  用潜状态比较候选未来，提供世界模型参与低延迟规划的实际闭环。

  <details>
  <summary>brief</summary>

  - **问题**：机载导航需评估多个候选路径，但世界模型计算预算有限。
  - **方法**：共享视觉特征编码，用多时域潜在预测评估候选动作轨迹。
  - **价值**：降低重复编码成本，改善实地视觉导航的路径选择。
  - **局限**：真实测试规模较小，嵌入式推理延迟仍限制快速闭环应用。

  来源：<a href="https://arxiv.org/abs/2610.12368">[1]</a> · <a href="https://arxiv.org/pdf/2610.12368">[2]</a>
  核验：2026-10-13

  </details>

+ [PLaW-VLA: Predictive Latent World Modeling for Vision-Language-Action Policies](<https://arxiv.org/abs/2610.12285>)<br>
  [![Star](https://img.shields.io/github/stars/RainyRobo/PLaW-VLA.svg?style=social&label=Star)](<https://github.com/RainyRobo/PLaW-VLA>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.12285>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://rainyrobo.github.io/PLaW-VLA>)
  <br>2026-10-08 · VLA / 世界模型 / 未来状态 / 长程控制

  **[CoRL 2026](<https://arxiv.org/abs/2610.12285>)** · **P0 必读** · 摘要与引言
  研究该预测什么未来以及如何用于动作，适合比较生成式和表征式世界模型。

  <details>
  <summary>brief</summary>

  - **问题**：视觉语言动作策略需要提前感知未来，当前观测不足以规划。
  - **方法**：在冻结视觉编码器空间预测未来状态，由动作专家联合读取。
  - **价值**：将潜在世界预测接入策略训练，实验显示控制表现改善。
  - **局限**：官方预训练权重仍待发布，额外模块耗时不等于端到端延迟。

  来源：<a href="https://arxiv.org/abs/2610.12285">[1]</a> · <a href="https://arxiv.org/pdf/2610.12285">[2]</a> · <a href="https://github.com/RainyRobo/PLaW-VLA">[3]</a> · <a href="https://rainyrobo.github.io/PLaW-VLA">[4]</a>
  核验：2026-10-13

  </details>

+ [UNITAS: A 3D-Native World Action Model for Embodied Manipulation](<https://arxiv.org/abs/2610.12099>)<br>
  [![Star](https://img.shields.io/github/stars/DexForce/UNITAS.svg?style=social&label=Star)](<https://github.com/DexForce/UNITAS>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.12099>)
  <br>2026-10-08 · 三维状态 / 世界模型 / 动作流 / 场景流

  **arXiv 预印本（录用待核实）** · **P0 必读** · 摘要与引言
  在统一三维坐标中联结动作与场景变化，是世界模型状态表示的重要对照路线。

  <details>
  <summary>brief</summary>

  - **问题**：二维视觉与动作表示分离，难以统一建模空间变化和控制。
  - **方法**：在统一度量空间建模三维场景与动作点轨迹，使用双专家流模型。
  - **价值**：探索三维原生世界动作建模以支持具身操作。
  - **局限**：世界模型带来的独立收益仍有限，完整实现的发布状态需关注。

  来源：<a href="https://arxiv.org/abs/2610.12099">[1]</a> · <a href="https://arxiv.org/pdf/2610.12099">[2]</a> · <a href="https://github.com/DexForce/UNITAS">[3]</a>
  核验：2026-10-13

  </details>

+ [RoboJEPA: Scaling Robotic Latent World Models](<https://arxiv.org/abs/2610.10515>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.10515>)
  <br>2026-10-07 · 潜空间世界模型 / 缩放规律 / 规划

  **arXiv 预印本（录用待核实）** · **P0 必读** · 摘要与引言
  研究潜空间预测误差能否预示实际规划收益，是评估世界模型可用性的核心问题。

  <details>
  <summary>brief</summary>

  - **问题**：像素世界模型规划成本高，潜空间模型的规模收益尚待检验。
  - **方法**：扩展机器人潜在预测模型，以目标图像引导闭环动作规划。
  - **价值**：展示大规模潜空间预测用于控制的潜力并优化规划计算。
  - **局限**：多步规划仍有明显延迟，不能直接视为实时控制方案。

  来源：<a href="https://arxiv.org/abs/2610.10515">[1]</a> · <a href="https://arxiv.org/pdf/2610.10515">[2]</a>
  核验：2026-10-13

  </details>

+ [DepthWorld: 3D World Model for Robot Manipulation](<https://arxiv.org/abs/2610.08780>)<br>
  [![Star](https://img.shields.io/github/stars/Jai2500/depthworld.svg?style=social&label=Star)](<https://github.com/Jai2500/depthworld>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.08780>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://jaibardhan.com/depthworld>) [![Weights](https://img.shields.io/badge/Weights-yellow.svg)](<https://huggingface.co/jaibrdhn/depthworld>)
  <br>2026-10-06 · 世界模型 / 几何一致性 / 深度监督

  **[CoRL 2026](<https://arxiv.org/abs/2610.08780>)** · **P0 必读** · 摘要与引言
  联合 RGB 与深度预测直接检验世界模型的几何一致性，而非仅比较画面质量。

  <details>
  <summary>brief</summary>

  - **问题**：机器人视频世界模型容易产生跨视角不一致的三维几何。
  - **方法**：重新校准多视角数据，联合预测动作条件下的彩色图像与深度。
  - **价值**：改善空间一致性，开放模型权重与标定资源供复现。
  - **局限**：预测质量提升尚不等于策略控制收益，部分数据需申请访问。

  来源：<a href="https://arxiv.org/abs/2610.08780">[1]</a> · <a href="https://arxiv.org/pdf/2610.08780">[2]</a> · <a href="https://github.com/Jai2500/depthworld">[3]</a> · <a href="https://huggingface.co/jaibrdhn/depthworld">[4]</a> · <a href="https://jaibardhan.com/depthworld">[5]</a>
  核验：2026-10-13

  </details>

+ [OpenWAM: An Open Framework for Composable World-Action Models](<https://arxiv.org/abs/2610.07922>)<br>
  [![Star](https://img.shields.io/github/stars/OpenWAM/OpenWAM.svg?style=social&label=Star)](<https://github.com/OpenWAM/OpenWAM>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.07922>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://openwam.stanford.edu/>) [![Weights](https://img.shields.io/badge/Weights-yellow.svg)](<https://huggingface.co/OpenWAM-Stanford/OpenWAM-Pretraining>)
  <br>2026-10-06 · 世界动作模型 / 反事实数据 / 因果视频 / 模块复用

  **arXiv 预印本（录用待核实）** · **P0 必读** · 摘要与引言
  提供可控比较视频与动作耦合方式的平台，适合研究世界模型如何支持规划与执行。

  <details>
  <summary>brief</summary>

  - **问题**：世界模型与动作策略常各自训练，组件难以跨任务组合复用。
  - **方法**：共享因果视频骨干，比较视频动作生成顺序并组合正逆动力学。
  - **价值**：提供统一框架和反事实数据训练路径，便于研究组件复用。
  - **局限**：数据量差异影响归因，仿真复用不等于真实机器人零样本迁移。

  来源：<a href="https://arxiv.org/abs/2610.07922">[1]</a> · <a href="https://arxiv.org/pdf/2610.07922">[2]</a> · <a href="https://github.com/OpenWAM/OpenWAM">[3]</a> · <a href="https://huggingface.co/OpenWAM-Stanford/OpenWAM-Pretraining">[4]</a> · <a href="https://openwam.stanford.edu/">[5]</a>
  核验：2026-10-13

  </details>

+ [WorldCompass: Reinforcement Learning for Long-Horizon World Models](<https://arxiv.org/abs/2602.09022>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2602.09022>)
  <br>2026-02-09 · 世界模型 / 动作控制 / 强化学习 / 长时一致性

  **[ICML 2026](<https://proceedings.mlr.press/v306/wang26iu.html>)** · **P0 必读** · 摘要与引言
  直接研究长时交互世界模型的动作遵循、曝光偏差和后训练，是主线必读。

  <details>
  <summary>brief</summary>

  - **问题**：仅用像素监督预训练的世界模型，长时间交互时容易偏离动作并累积错误。
  - **方法**：在目标片段采样多条候选，以动作准确性和视觉质量互补奖励进行负样本感知优化。
  - **价值**：将细粒度反馈与自身生成历史结合，为世界模型后训练提供完整切入点。
  - **局限**：主要在 WorldPlay 上验证，跨模型迁移和真实环境闭环能力仍待检验。

  来源：<a href="https://arxiv.org/abs/2602.09022">[1]</a> · <a href="https://arxiv.org/pdf/2602.09022">[2]</a> · <a href="https://proceedings.mlr.press/v306/wang26iu.html">[3]</a>
  核验：2026-10-13

  </details>

+ [WorldPlay: Towards Long-Term Geometric Consistency for Real-Time Interactive World Modeling](<https://arxiv.org/abs/2512.14614>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2512.14614>)
  <br>2025-12-16 · 世界模型 / 实时交互 / 空间记忆 / 蒸馏

  **[ICML 2026](<https://proceedings.mlr.press/v306/sun26az.html>)** · **P0 必读** · 摘要与引言
  同时处理交互速度、空间记忆和蒸馏，是世界模型与实时生成交叉点的核心论文。

  <details>
  <summary>brief</summary>

  - **问题**：实时世界模型常在快速生成与重访场景的一致性之间取舍。
  - **方法**：结合离散动作和连续位姿检索历史帧，重置记忆时间位置，并对齐师生记忆上下文进行蒸馏。
  - **价值**：将状态记忆、控制和加速联合设计，为长时交互生成提供系统基线。
  - **局限**：展示的帧率依赖运行配置，几何一致性也不能替代真实动力学与因果评测。

  来源：<a href="https://arxiv.org/abs/2512.14614">[1]</a> · <a href="https://arxiv.org/pdf/2512.14614">[2]</a> · <a href="https://proceedings.mlr.press/v306/sun26az.html">[3]</a>
  核验：2026-10-13

  </details>

+ [Video-GPT via Next Clip Diffusion](<https://arxiv.org/abs/2505.12489>)<br>
  [![Star](https://img.shields.io/github/stars/zhuangshaobin/Video-GPT.svg?style=social&label=Star)](<https://github.com/zhuangshaobin/Video-GPT>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2505.12489>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://video-gpt.github.io/>)
  <br>2025-05-18 · 世界模型 / 自回归扩散 / 视频生成

  **[ICLR 2026](<https://github.com/zhuangshaobin/Video-GPT>)** · **P0 必读** · 摘要与引言
  下一片段扩散直接连接视频生成与世界预测，适合作为后续交互和记忆机制的基线。

  <details>
  <summary>brief</summary>

  - **问题**：语言难完整承载视觉动态，纯扩散或离散自回归又难兼顾预测时长与生成质量。
  - **方法**：把视频片段作为建模单元，在干净历史条件下对下一带噪片段逐步去噪。
  - **价值**：用统一预训练任务连接短时生成、长期预测及下游视频理解。
  - **局限**：基于干净历史的训练仍有曝光偏差，预测成绩不能替代动作条件下的闭环验证。

  来源：<a href="https://arxiv.org/abs/2505.12489">[1]</a> · <a href="https://arxiv.org/pdf/2505.12489">[2]</a> · <a href="https://github.com/zhuangshaobin/Video-GPT">[3]</a> · <a href="https://video-gpt.github.io/">[4]</a>
  核验：2026-10-13

  </details>

+ [Dex-One2Many: Learning Dexterous Manipulation from a Single Human Demonstration](<https://arxiv.org/abs/2610.12470>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.12470>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://dex-one2many.github.io/>)
  <br>2026-10-08 · 任务抽象 / 场景图 / 示范学习

  **arXiv 预印本（录用待核实）** · **P1 重点** · 摘要与引言
  场景图将示范转成任务约束，可借鉴规划状态抽象，但主要研究灵巧操作。

  <details>
  <summary>brief</summary>

  - **问题**：单个人类示范难以覆盖灵巧操作所需的场景与动作变化。
  - **方法**：从视频提取场景图，构造多样仿真初态和奖励并训练强化策略。
  - **价值**：将单次示范扩展为训练任务，支持仿真到真实操作迁移。
  - **局限**：仍需资产、抓取及姿态准备，不代表同一策略零样本跨形态泛化。

  来源：<a href="https://arxiv.org/abs/2610.12470">[1]</a> · <a href="https://arxiv.org/pdf/2610.12470">[2]</a> · <a href="https://dex-one2many.github.io/">[3]</a>
  核验：2026-10-13

  </details>

+ [RESETTLE: Robotic Recovery through Disagreement-Triggered Retrieval and Efficient Corrective Control](<https://arxiv.org/abs/2610.12185>)<br>
  [![Star](https://img.shields.io/github/stars/JIA-Lab-research/RESETTLE.svg?style=social&label=Star)](<https://github.com/JIA-Lab-research/RESETTLE>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.12185>)
  <br>2026-10-08 · 失败恢复 / 示范检索 / 闭环控制

  **arXiv 预印本（录用待核实）** · **P1 重点** · 摘要与引言
  检索示范进行局部恢复可补充高层规划，但控制层机制并非通用 Agent 记忆。

  <details>
  <summary>brief</summary>

  - **问题**：机器人策略遇到失误后缺少可靠的触发机制与恢复控制。
  - **方法**：以动作采样分歧触发成功经验检索，并执行带约束的纠正动作。
  - **价值**：为既有策略增加恢复能力，减少偏离后的连续失败。
  - **局限**：一致但错误的预测可能漏检，模块计时不等于完整系统延迟。

  来源：<a href="https://arxiv.org/abs/2610.12185">[1]</a> · <a href="https://arxiv.org/pdf/2610.12185">[2]</a> · <a href="https://github.com/JIA-Lab-research/RESETTLE">[3]</a>
  核验：2026-10-13

  </details>

+ [PointWAM: 3D World Action Modeling for Dexterous Robotic Manipulation](<https://arxiv.org/abs/2610.02840>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.02840>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://chrockey.github.io/PointWAM>)
  <br>2026-10-02 · 三维轨迹 / 世界动作模型 / 人类示范 / 灵巧操作

  **arXiv 预印本（录用待核实）** · **P1 重点** · 摘要与引言
  共享三维点轨迹连接环境预测与动作生成，适合作为像素世界模型的表征对照。

  <details>
  <summary>brief</summary>

  - **问题**：灵巧操作需要理解三维场景变化，单纯动作模仿难以迁移。
  - **方法**：联合预测场景点与手部关键点，再将动作重定向到机器人。
  - **价值**：利用人类视频预训练和三维监督连接世界预测与操作。
  - **局限**：依赖重定向及场景准备，精细接触任务的成功率仍有限。

  来源：<a href="https://arxiv.org/abs/2610.02840">[1]</a> · <a href="https://arxiv.org/pdf/2610.02840">[2]</a> · <a href="https://chrockey.github.io/PointWAM">[3]</a>
  核验：2026-10-13

  </details>


## 交互 Avatar

+ [PixReenact: Pixel-Conditioned Causal Video Diffusion for Streaming Head-Avatar Reenactment](<https://arxiv.org/abs/2610.05233>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2610.05233>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://gavriel-habib.github.io/pixreenact>)
  <br>2026-10-04 · 双教师蒸馏 / 因果扩散 / 流式Avatar / 身份保持

  **arXiv 预印本（录用待核实）** · **P0 必读** · 摘要与引言
  像素驱动、双教师与流式蒸馏直接面向实时 Avatar，应重点区分吞吐和交互延迟。

  <details>
  <summary>brief</summary>

  - **问题**：流式头像重演需同时维持身份和跟随驱动视频的头部运动。
  - **方法**：采用像素条件因果扩散、跨身份伪监督及双教师蒸馏。
  - **价值**：以少步分块生成支持低延迟头部头像重演。
  - **局限**：研究范围主要是头部，不等于全身控制或对话交互。

  来源：<a href="https://arxiv.org/abs/2610.05233">[1]</a> · <a href="https://arxiv.org/pdf/2610.05233">[2]</a> · <a href="https://gavriel-habib.github.io/pixreenact">[3]</a>
  核验：2026-10-13

  </details>

+ [StreamAvatar: Streaming Diffusion Models for Real-Time Interactive Human Avatars](<https://arxiv.org/abs/2512.22065>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2512.22065>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://streamavatar.github.io/>)
  <br>2025-12-26 · Avatar / 实时交互 / 流式生成 / 长期一致性

  **[CVPR 2026](<https://openaccess.thecvf.com/content/CVPR2026/html/Sun_StreamAvatar_Streaming_Diffusion_Models_for_Real-Time_Interactive_Human_Avatars_CVPR_2026_paper.html>)** · **P0 必读** · 摘要与引言
  最贴近实时交互 Avatar，优先研究流式蒸馏、倾听与长期稳定。

  <details>
  <summary>brief</summary>

  - **问题**：高质量数字人扩散模型非因果且慢，长时间运行还会身份漂移。
  - **方法**：先训练说话倾听教师，再进行块因果蒸馏和一致性判别器精修，保留参考锚点。
  - **价值**：支持音频流驱动的连续表情、手势和说听切换。
  - **局限**：端到端延迟仍取决于音频及分块设置，超长交互需单独检验。

  来源：<a href="https://arxiv.org/abs/2512.22065">[1]</a> · <a href="https://arxiv.org/pdf/2512.22065">[2]</a> · <a href="https://openaccess.thecvf.com/content/CVPR2026/html/Sun_StreamAvatar_Streaming_Diffusion_Models_for_Real-Time_Interactive_Human_Avatars_CVPR_2026_paper.html">[3]</a> · <a href="https://streamavatar.github.io/">[4]</a>
  核验：2026-10-13

  </details>

+ [ActAvatar: Temporally-Aware Precise Action Control for Talking Avatars](<https://arxiv.org/abs/2512.19546>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2512.19546>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://ziqiaopeng.github.io/ActAvatar>)
  <br>2025-12-22 · Avatar / 动作控制 / 时间控制 / 音画同步

  **[CVPR 2026](<https://openaccess.thecvf.com/content/CVPR2026/html/Peng_ActAvatar_Temporally-Aware_Precise_Action_Control_for_Talking_Avatars_CVPR_2026_paper.html>)** · **P0 必读** · 摘要与引言
  直接解决 Avatar 动作语义、时间定位与口型同步的协调。

  <details>
  <summary>brief</summary>

  - **问题**：说话数字人的动作常忽略文字或偏离对应语音时刻。
  - **方法**：按时间阶段组织提示，浅层侧重动作文本、深层强化音频，并分阶段训练。
  - **价值**：无需骨架即可对动作内容及发生时间进行控制。
  - **局限**：仍依赖显式阶段标注和给定音频，实时交互能力不能由离线质量推断。

  来源：<a href="https://arxiv.org/abs/2512.19546">[1]</a> · <a href="https://arxiv.org/pdf/2512.19546">[2]</a> · <a href="https://openaccess.thecvf.com/content/CVPR2026/html/Peng_ActAvatar_Temporally-Aware_Precise_Action_Control_for_Talking_Avatars_CVPR_2026_paper.html">[3]</a> · <a href="https://ziqiaopeng.github.io/ActAvatar">[4]</a>
  核验：2026-10-13

  </details>

+ [Stand-In: A Lightweight and Plug-and-Play Identity Control for Video Generation](<https://arxiv.org/abs/2508.07901>)<br>
  [![Star](https://img.shields.io/github/stars/WeChatCV/Stand-In.svg?style=social&label=Star)](<https://github.com/WeChatCV/Stand-In>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2508.07901>)
  <br>2025-08-11 · Avatar / 视频生成 / 身份保持 / 轻量适配

  **[CVPR 2026](<https://openaccess.thecvf.com/content/CVPR2026/html/Xue_Stand-In_A_Lightweight_and_Plug-and-Play_Identity_Control_for_Video_Generation_CVPR_2026_paper.html>)** · **P0 必读** · 摘要与引言
  轻量身份保持可直接支撑实时 Avatar 生成骨干。

  <details>
  <summary>brief</summary>

  - **问题**：身份定制常需大量参数训练，且难兼容已有视频控制工具。
  - **方法**：用同源潜空间编码参考图，通过受限自注意力和条件位置映射注入身份。
  - **价值**：以少量新增参数实现可插拔的主体保持。
  - **局限**：身份相似度不代表长时间动作和口型稳定，实时性能需与加速方法结合。

  来源：<a href="https://arxiv.org/abs/2508.07901">[1]</a> · <a href="https://arxiv.org/pdf/2508.07901">[2]</a> · <a href="https://github.com/WeChatCV/Stand-In">[3]</a> · <a href="https://openaccess.thecvf.com/content/CVPR2026/html/Xue_Stand-In_A_Lightweight_and_Plug-and-Play_Identity_Control_for_Video_Generation_CVPR_2026_paper.html">[4]</a>
  核验：2026-10-13

  </details>


## 智能体与上下文

+ [IterSynth: Rethinking Deep Search Agents via Role-Decoupled Iterative Synthesis](<https://arxiv.org/abs/2609.29444>)<br>
  [![Star](https://img.shields.io/github/stars/Tencent/IterSynth.svg?style=social&label=Star)](<https://github.com/Tencent/IterSynth>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2609.29444>)
  <br>2026-09-24 · Agent规划 / 上下文管理 / 增量摘要 / 过程奖励

  **[EMNLP 2026](<https://yanyc428.github.io/publication/2026-09-24-itersynth>)** · **P0 必读** · 已核对正文
  规划与增量摘要交替训练，直接切入 Agent 长任务中的记忆压缩和证据整合。

  <details>
  <summary>brief</summary>

  - **问题**：搜索规划与证据综合共用长历史，易受噪声与职责耦合影响。
  - **方法**：同一模型轮流规划和更新摘要，每轮重建上下文，并按角色独立归一化过程奖励。
  - **价值**：8B五项均分50.7，较仅结果奖励高1.8点。
  - **局限**：GAIA低于部分8B基线，摘要遗漏与裁判质量仍是边界。

  来源：<a href="https://arxiv.org/abs/2609.29444">[1]</a> · <a href="https://arxiv.org/pdf/2609.29444v1">[2]</a> · <a href="https://github.com/Tencent/IterSynth">[3]</a> · <a href="https://yanyc428.github.io/publication/2026-09-24-itersynth">[4]</a>
  核验：2026-10-13

  </details>

+ [ContextPilot: Teaching Agents for Proactive Context Management via Fine-grained RL](<https://arxiv.org/abs/2608.28476>)<br>
  [![Star](https://img.shields.io/github/stars/Tencent/ContextPilot.svg?style=social&label=Star)](<https://github.com/Tencent/ContextPilot>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2608.28476>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://tencent.github.io/ContextPilot>)
  <br>2026-08-28 · Agent记忆 / 上下文压缩 / 信用分配 / 强化学习

  **[EMNLP 2026](<https://arxiv.org/abs/2608.28476>)** · **P0 必读** · 已核对正文
  可恢复上下文折叠与细粒度信用分配，直接对应 Agent 主动记忆管理。

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
  <br>2026-08-06 · Agent调试 / 失败归因 / 经验记忆 / 轨迹压缩

  **[Findings of EMNLP 2026](<https://github.com/THU-KEG/TrajDebug>)** · **P0 必读** · 已核对正文
  区分局部错误、后续修复与最终失败根因，直接服务 Agent 规划调试和经验记忆。

  <details>
  <summary>brief</summary>

  - **问题**：长轨迹局部错误可能被修复或无害，最早出错不等于失败根因。
  - **方法**：分层压缩历史，以逐字证据识别冲突，按修复状态与终局影响筛选后归因。
  - **价值**：同骨干关键步骤准确率由25.69%升至34.11%。
  - **局限**：漏检会传播，最终归因仍依赖模型判断。

  来源：<a href="https://arxiv.org/abs/2608.06346">[1]</a> · <a href="https://arxiv.org/pdf/2608.06346v1">[2]</a> · <a href="https://github.com/THU-KEG/TrajDebug">[3]</a>
  核验：2026-10-13

  </details>

+ [Breaking Dual Bottlenecks: Evolving Unified Multimodal Models into Self-Adaptive Interleaved Visual Reasoners](<https://arxiv.org/abs/2605.14709>)<br>
  [![Star](https://img.shields.io/github/stars/WeChatCV/Interleaved_Visual_Reasoner.svg?style=social&label=Star)](<https://github.com/WeChatCV/Interleaved_Visual_Reasoner>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2605.14709>)
  <br>2026-05-14 · 生成Agent / 统一多模态 / 自适应规划 / 视觉反馈

  **[ICML 2026](<https://proceedings.mlr.press/v306/liu26ak.html>)** · **P0 必读** · 摘要与引言
  连接 Agent 规划、生成执行与视觉反馈，适合研究生成模型如何形成可纠错闭环。

  <details>
  <summary>brief</summary>

  - **问题**：模型理解编辑意图后仍可能执行失败，预先规划和无结构反思都缺少有效闭环。
  - **方法**：构建直接生成、反思修正和分步规划轨迹，以步骤奖励及复杂度惩罚训练策略切换。
  - **价值**：将选择何时思考、如何执行和何时返工统一为可学习流程。
  - **局限**：数据依赖强外部模型且集中图像任务，视频时序执行与实时延迟仍需验证。

  来源：<a href="https://arxiv.org/abs/2605.14709">[1]</a> · <a href="https://arxiv.org/pdf/2605.14709">[2]</a> · <a href="https://github.com/WeChatCV/Interleaved_Visual_Reasoner">[3]</a> · <a href="https://proceedings.mlr.press/v306/liu26ak.html">[4]</a>
  核验：2026-10-13

  </details>

+ [MASPO: Joint Prompt Optimization for LLM-based Multi-Agent Systems](<https://arxiv.org/abs/2605.06623>)<br>
  [![Star](https://img.shields.io/github/stars/wangzx1219/MASPO.svg?style=social&label=Star)](<https://github.com/wangzx1219/MASPO>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2605.06623>)
  <br>2026-05-07 · 协同规划 / 多Agent / 提示优化

  **[ICML 2026](<https://proceedings.mlr.press/v306/wang26ew.html>)** · **P0 必读** · 摘要与引言
  直接研究多 Agent 中局部成功却整体失败的规划协作问题，值得重点读评价与归因设计。

  <details>
  <summary>brief</summary>

  - **问题**：各 Agent 满足局部指令仍可能误导下游，独立优化提示难改善整体任务。
  - **方法**：联合评估局部有效性、后续潜力和全局目标，挖掘失配轨迹并交替进化提示。
  - **价值**：将优化目标从单个输出转向协作链，为规划系统调试提供方法。
  - **局限**：依赖模型评价代理和既定协作结构，复杂环境中的泛化及优化成本需再检验。

  来源：<a href="https://arxiv.org/abs/2605.06623">[1]</a> · <a href="https://arxiv.org/pdf/2605.06623">[2]</a> · <a href="https://github.com/wangzx1219/MASPO">[3]</a> · <a href="https://proceedings.mlr.press/v306/wang26ew.html">[4]</a>
  核验：2026-10-13

  </details>

+ [AdapTime: Enabling Adaptive Temporal Reasoning in Large Language Models](<https://arxiv.org/abs/2604.24175>)<br>
  [![Star](https://img.shields.io/github/stars/Applied-Machine-Learning-Lab/ACL2026-AdapTime.svg?style=social&label=Star)](<https://github.com/Applied-Machine-Learning-Lab/ACL2026-AdapTime>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2604.24175>)
  <br>2026-04-27 · Agent规划 / 事件记忆 / 时间推理

  **[Findings of ACL 2026](<https://aclanthology.org/2026.findings-acl.1621>)** · **P0 必读** · 摘要与引言
  时间关系与按需推理直接影响 Agent 事件记忆、历史检索及计划判断。

  <details>
  <summary>brief</summary>

  - **问题**：固定时间推理流程对简单问题过度处理，对复杂事件关系又可能分析不足。
  - **方法**：由语言模型规划器按上下文选择重构、改写和复核步骤，动态调整推理路径。
  - **价值**：提供无需外部执行工具的时间推理基线，便于接入事件记忆查询。
  - **局限**：主要在文本时间问答中验证，真实记忆冲突、时间更新和长程行动尚未覆盖。

  来源：<a href="https://aclanthology.org/2026.findings-acl.1621">[1]</a> · <a href="https://arxiv.org/abs/2604.24175">[2]</a> · <a href="https://arxiv.org/pdf/2604.24175">[3]</a> · <a href="https://github.com/Applied-Machine-Learning-Lab/ACL2026-AdapTime">[4]</a>
  核验：2026-10-13

  </details>

+ [Planning Beyond Text: Graph-based Reasoning for Complex Narrative Generation](<https://arxiv.org/abs/2604.21253>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2604.21253>)
  <br>2026-04-23 · 事件图 / 人物一致性 / 叙事规划 / 多Agent

  **[Findings of ACL 2026](<https://aclanthology.org/2026.findings-acl.1874>)** · **P0 必读** · 摘要与引言
  事件图与角色图可连接长视频叙事、交互 Avatar 和 Agent 的显式规划记忆。

  <details>
  <summary>brief</summary>

  - **问题**：直接在长文本上规划容易丢失事件因果和人物动机，导致叙事结构断裂。
  - **方法**：在事件图和角色图上循环评估、规划与修订，通过受约束的图编辑先修复骨架再生成文本。
  - **价值**：将全局一致性转成可检查的结构操作，适合研究长程生成规划。
  - **局限**：当前验证文本叙事，图约束如何落实到镜头、动作和连续视频仍需连接执行器。

  来源：<a href="https://aclanthology.org/2026.findings-acl.1874">[1]</a> · <a href="https://arxiv.org/abs/2604.21253">[2]</a> · <a href="https://arxiv.org/pdf/2604.21253">[3]</a>
  核验：2026-10-13

  </details>

+ [Guaranteeing Knowledge Integration with Joint Decoding for Retrieval-Augmented Generation](<https://arxiv.org/abs/2604.08046>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2604.08046>)
  <br>2026-04-09 · 检索增强 / 知识冲突 / 联合解码 / 记忆使用

  **[ACL 2026](<https://aclanthology.org/2026.acl-long.192>)** · **P0 必读** · 摘要与引言
  直接针对 Agent 外部记忆与参数知识冲突，应和检索、记忆压缩论文一起读。

  <details>
  <summary>brief</summary>

  - **问题**：即使检索正确，模型仍可能被内部先验覆盖或生硬拼接证据。
  - **方法**：分离内部推理答案与证据答案，以对比偏好训练抑制先验干扰，再逐词联合解码。
  - **价值**：把记忆检索后的整合瓶颈显式化，便于设计可诊断的知识使用流程。
  - **局限**：依赖检索证据可靠性且增加生成成本，名称中的保证不代表普遍正确性证明。

  来源：<a href="https://aclanthology.org/2026.acl-long.192">[1]</a> · <a href="https://arxiv.org/abs/2604.08046">[2]</a> · <a href="https://arxiv.org/pdf/2604.08046">[3]</a>
  核验：2026-10-13

  </details>

+ [Figure It Out: Improve the Frontier of Reasoning with Executable Visual States](<https://arxiv.org/abs/2512.24297>)<br>
  [![Star](https://img.shields.io/github/stars/chenmeiqii/FIGR.svg?style=social&label=Star)](<https://github.com/chenmeiqii/FIGR>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2512.24297>)
  <br>2025-12-30 · 可执行状态 / 工具推理 / 强化学习 / 视觉规划

  **[ACL 2026](<https://aclanthology.org/2026.acl-long.1827>)** · **P0 必读** · 摘要与引言
  可执行中间视觉状态直接连接规划、外部工作记忆和反馈闭环，是 Agent 主线重点。

  <details>
  <summary>brief</summary>

  - **问题**：文本推理难维持全局几何约束，自由生成图像又缺少精确可控的中间状态。
  - **方法**：在多轮推理中生成绘图代码并执行，将可修改图形作为反馈，用自适应奖励选择何时绘制。
  - **价值**：提供可检查、可修正的外部状态表示，连接符号计划与视觉观察。
  - **局限**：证据主要来自数学问题，复杂环境动力学与长期执行可靠性仍需扩展。

  来源：<a href="https://aclanthology.org/2026.acl-long.1827">[1]</a> · <a href="https://arxiv.org/abs/2512.24297">[2]</a> · <a href="https://arxiv.org/pdf/2512.24297">[3]</a> · <a href="https://github.com/chenmeiqii/FIGR">[4]</a>
  核验：2026-10-13

  </details>

+ [From Final Artifacts to Trajectories: Retrospective Process Supervision for Evidence-Grounded Long-Form Generation](<https://arxiv.org/abs/2608.30461>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2608.30461>)
  <br>2026-08-31 · Agent训练 / 检索规划 / 轨迹合成 / 过程监督

  **arXiv 预印本（录用待核实）** · **P1 重点** · 已核对正文
  从高质量产物恢复可执行检索轨迹，为训练规划与工具使用 Agent 提供数据路线。

  <details>
  <summary>brief</summary>

  - **问题**：专家成品丰富，真实检索写作轨迹却稀缺。
  - **方法**：从成品反推任务并实际执行检索，以四维评分过滤，用验证后的合成稿配对轨迹训练。
  - **价值**：同预算对照显示过程监督优于仅模仿最终产物。
  - **局限**：恢复的是合理候选过程；效果依赖成品中可追溯的证据。

  来源：<a href="https://arxiv.org/abs/2608.30461">[1]</a> · <a href="https://arxiv.org/pdf/2608.30461v1">[2]</a>
  核验：2026-10-13

  </details>

+ [Semantic-Enriched Latent Visual Reasoning](<https://arxiv.org/abs/2605.19342>)<br>
  [![Star](https://img.shields.io/github/stars/tinnel123666888/slvr.svg?style=social&label=Star)](<https://github.com/tinnel123666888/slvr>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2605.19342>)
  <br>2026-05-19 · 多查询训练 / 潜空间推理 / 视觉状态

  **[ICML 2026](<https://proceedings.mlr.press/v306/xu26aw.html>)** · **P1 重点** · 摘要与引言
  区域级语义潜变量可作为 Agent 紧凑视觉状态的候选表示。

  <details>
  <summary>brief</summary>

  - **问题**：仅由视觉监督得到的潜变量可能保留外观，却缺乏支持多类问题的语义属性。
  - **方法**：先用区域属性丰富潜变量，再对同一区域的多个问题联合进行策略优化。
  - **价值**：为紧凑视觉表征应保留哪些信息提供可测量训练目标。
  - **局限**：验证集中于区域问答，尚不覆盖时间变化、长期记忆更新或行动结果预测。

  来源：<a href="https://arxiv.org/abs/2605.19342">[1]</a> · <a href="https://arxiv.org/pdf/2605.19342">[2]</a> · <a href="https://github.com/tinnel123666888/slvr">[3]</a> · <a href="https://proceedings.mlr.press/v306/xu26aw.html">[4]</a>
  核验：2026-10-13

  </details>

+ [FinToolSyn: A forward synthesis Framework for Financial Tool-Use Dialogue Data with Dynamic Tool Retrieval](<https://arxiv.org/abs/2603.24051>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2603.24051>)
  <br>2026-03-25 · 动态检索 / 工具Agent / 数据合成

  **[Findings of ACL 2026](<https://aclanthology.org/2026.findings-acl.746>)** · **P1 重点** · 摘要与引言
  从真实模糊需求到动态工具检索的流程，与 Agent 规划及澄清能力直接相关。

  <details>
  <summary>brief</summary>

  - **问题**：从预选工具反推问题会泄露参数与解法，静态候选集也掩盖真实工具检索困难。
  - **方法**：从角色需求正向合成多轮对话，构建大工具库并注入动态检索候选与执行前检查。
  - **价值**：为训练澄清、检索和调用时机提供更接近交互过程的数据方案。
  - **局限**：仍是金融领域合成工具环境，跨领域迁移和真实服务错误处理需要验证。

  来源：<a href="https://aclanthology.org/2026.findings-acl.746">[1]</a> · <a href="https://arxiv.org/abs/2603.24051">[2]</a> · <a href="https://arxiv.org/pdf/2603.24051">[3]</a>
  核验：2026-10-13

  </details>

+ [RouteMoA: Dynamic Routing without Pre-Inference Boosts Efficient Mixture-of-Agents](<https://arxiv.org/abs/2601.18130>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2601.18130>)
  <br>2026-01-26 · 动态路由 / 多Agent / 推理加速

  **[ACL 2026](<https://aclanthology.org/2026.acl-long.558>)** · **P1 重点** · 摘要与引言
  多 Agent 的延迟与成本直接影响实时交互，可与 MASPO 的质量优化互补阅读。

  <details>
  <summary>brief</summary>

  - **问题**：先调用全部模型再筛选结果，难真正降低多代理协作成本和等待时间。
  - **方法**：先由轻量评分器预测适合模型，再复用已有回答进行自评互评，综合质量和成本路由。
  - **价值**：将选择模型前移到推理之前，为动态协作提供效率基线。
  - **局限**：依赖候选模型能力预测，模型池变化和复杂交互任务可能改变路由效果。

  来源：<a href="https://aclanthology.org/2026.acl-long.558">[1]</a> · <a href="https://arxiv.org/abs/2601.18130">[2]</a> · <a href="https://arxiv.org/pdf/2601.18130">[3]</a>
  核验：2026-10-13

  </details>

+ [MIND: Multi-rationale INtegrated Discriminative Reasoning Framework for Multi-modal Large Models](<https://arxiv.org/abs/2512.05530>)<br>
  [![Star](https://img.shields.io/github/stars/YuChuang1205/MIND.svg?style=social&label=Star)](<https://github.com/YuChuang1205/MIND>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2512.05530>)
  <br>2025-12-05 · 多模态推理 / 对比学习 / 自我纠错

  **[ICML 2026](<https://proceedings.mlr.press/v306/yu26bv.html>)** · **P1 重点** · 摘要与引言
  正反推理链与纠错训练可用于 Agent 计划审查，但要区分离线纠错和在线自我修复。

  <details>
  <summary>brief</summary>

  - **问题**：单一正确推理链监督使模型难辨识误导解释，缺少主动纠错能力。
  - **方法**：生成多种正反理由，先学习正向推理再训练判别纠错，并用对比约束分离语义冲突。
  - **价值**：为构造可批判自身候选方案的多模态推理模型提供训练路线。
  - **局限**：主要来自静态问答，交互环境中错误发现与恢复能力需要另行评测。

  来源：<a href="https://arxiv.org/abs/2512.05530">[1]</a> · <a href="https://arxiv.org/pdf/2512.05530">[2]</a> · <a href="https://github.com/YuChuang1205/MIND">[3]</a> · <a href="https://proceedings.mlr.press/v306/yu26bv.html">[4]</a>
  核验：2026-10-13

  </details>

+ [GRAPE: Let GRPO Supervise Query Rewriting by Ranking for Retrieval](<https://arxiv.org/abs/2509.23370>)<br>
  [![Star](https://img.shields.io/github/stars/mogulzhang/GRAPE.svg?style=social&label=Star)](<https://github.com/mogulzhang/GRAPE>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2509.23370>)
  <br>2025-09-27 · 强化学习 / 查询改写 / 检索增强

  **[ICML 2026](<https://proceedings.mlr.press/v306/zhang26jn.html>)** · **P1 重点** · 摘要与引言
  固定检索库上的查询优化适合 Agent 记忆检索，尤其可借鉴防止奖励投机的设计。

  <details>
  <summary>brief</summary>

  - **问题**：冻结的图文检索器难适应长查询及跨语言输入，重建大型索引成本高。
  - **方法**：保留检索器和索引，用语料相对排名奖励训练查询改写模型，抑制相似度虚高。
  - **价值**：将查询适配与记忆库更新解耦，为已有检索系统提供增量改进路径。
  - **局限**：依赖可用相关性反馈，单轮召回提升尚不等于多轮记忆使用更有效。

  来源：<a href="https://arxiv.org/abs/2509.23370">[1]</a> · <a href="https://arxiv.org/pdf/2509.23370">[2]</a> · <a href="https://github.com/mogulzhang/GRAPE">[3]</a> · <a href="https://proceedings.mlr.press/v306/zhang26jn.html">[4]</a>
  核验：2026-10-13

  </details>

+ [TGPO: Efficient Policy Optimization through Sequence Anchor and Information Gating](<https://raw.githubusercontent.com/mlresearch/v306/main/assets/ding26i/ding26i.pdf>)<br>
  [![Paper](https://img.shields.io/badge/Paper-b31b1b.svg)](<https://raw.githubusercontent.com/mlresearch/v306/main/assets/ding26i/ding26i.pdf>)
  <br>日期待核实 · 信用分配 / 强化学习 / 训练稳定性

  **[ICML 2026](<https://proceedings.mlr.press/v306/ding26i.html>)** · **P1 重点** · 摘要与引言
  为 Agent 结果奖励训练提供更稳定的细粒度更新，适合作为规划后训练工具阅读。

  <details>
  <summary>brief</summary>

  - **问题**：整句重要性采样浪费局部有效梯度，逐词更新又容易被极端比率主导。
  - **方法**：以序列统计作为更新锚点，按整体漂移和内部一致性调节词级信息门控。
  - **价值**：保留不完美轨迹中的训练信号，连接稳定优化与样本利用效率。
  - **局限**：主要验证数学推理，不能据此断言解决了多步交互规划的信用分配。

  来源：<a href="https://proceedings.mlr.press/v306/ding26i.html">[1]</a> · <a href="https://raw.githubusercontent.com/mlresearch/v306/main/assets/ding26i/ding26i.pdf">[2]</a>
  核验：2026-10-13

  </details>

+ [Collision to Cognition: Hash-Driven Graph Construction for Efficient RAG](<https://aclanthology.org/2026.acl-long.1156.pdf>)<br>
  [![Paper](https://img.shields.io/badge/Paper-b31b1b.svg)](<https://aclanthology.org/2026.acl-long.1156.pdf>)
  <br>日期待核实 · 图检索 / 记忆索引 / 高效检索

  **[ACL 2026](<https://aclanthology.org/2026.acl-long.1156>)** · **P1 重点** · 摘要与引言
  低成本构建外部记忆图有实用价值，重点比较索引速度与关系表达损失。

  <details>
  <summary>brief</summary>

  - **问题**：语言模型抽取三元组或摘要建图成本高，单一聚类也限制文本的多重角色。
  - **方法**：利用局部敏感哈希碰撞同时形成片段连接和语义社区，替代昂贵的神经建图流程。
  - **价值**：减少外部知识结构化所需的模型调用与硬件开销。
  - **局限**：哈希相似连接并非因果或逻辑证明，细粒度语义和跨语言关系仍可能遗漏。

  来源：<a href="https://aclanthology.org/2026.acl-long.1156">[1]</a> · <a href="https://aclanthology.org/2026.acl-long.1156.pdf">[2]</a>
  核验：2026-10-13

  </details>

+ [Query-Aware Knowledge Retrieval via Hyperbolic Structuring](<https://aclanthology.org/2026.acl-long.986.pdf>)<br>
  [![Paper](https://img.shields.io/badge/Paper-b31b1b.svg)](<https://aclanthology.org/2026.acl-long.986.pdf>)
  <br>日期待核实 · 关系记忆 / 图检索 / 多跳推理

  **[ACL 2026](<https://aclanthology.org/2026.acl-long.986>)** · **P1 重点** · 摘要与引言
  查询驱动关系建模适合多跳记忆检索，可与固定图索引方法对比。

  <details>
  <summary>brief</summary>

  - **问题**：静态知识图通常按全局主题连边，难捕捉特定问题隐含的推理关系。
  - **方法**：结合实体连接与查询分解出的关系线索，将局部最小子树在双曲空间中统一建模。
  - **价值**：让检索结构适应当前问题，为关系型外部记忆提供思路。
  - **局限**：查询解析与图构建错误会传播，动态图维护及长期新增记忆成本需另测。

  来源：<a href="https://aclanthology.org/2026.acl-long.986">[1]</a> · <a href="https://aclanthology.org/2026.acl-long.986.pdf">[2]</a>
  核验：2026-10-13

  </details>

+ [Progressive Re-ranking for Multimodal Retrieval-Augmented Generation via Curriculum Learning](<https://aclanthology.org/2026.findings-acl.2045.pdf>)<br>
  [![Paper](https://img.shields.io/badge/Paper-b31b1b.svg)](<https://aclanthology.org/2026.findings-acl.2045.pdf>)
  <br>日期待核实 · 多模态检索 / 记忆检索 / 难负样本

  **[Findings of ACL 2026](<https://aclanthology.org/2026.findings-acl.2045>)** · **P1 重点** · 摘要与引言
  多模态记忆的相似实体混淆是实际瓶颈，分层重排可作为检索后处理基线。

  <details>
  <summary>brief</summary>

  - **问题**：视觉粗检索容易找到外观相似但事实不匹配的实体，干扰后续回答。
  - **方法**：先做细粒度段落重排，再进行多模态复核，用逐步加难的误导性负样本训练。
  - **价值**：将实体召回与具体证据定位分开，提升外部知识使用前的筛选精度。
  - **局限**：多阶段重排增加延迟，效果受初始召回覆盖与负样本分布限制。

  来源：<a href="https://aclanthology.org/2026.findings-acl.2045">[1]</a> · <a href="https://aclanthology.org/2026.findings-acl.2045.pdf">[2]</a>
  核验：2026-10-13

  </details>

+ [Intent-Driven Semantic ID Generation for Grounded Conversational News Recommendation](<https://arxiv.org/abs/2605.07613>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2605.07613>)
  <br>2026-05-08 · 个性化 / 意图建模 / 生成式检索

  **[ACL 2026 Industry](<https://aclanthology.org/2026.acl-industry.130>)** · **P2 选读** · 摘要与引言
  隐含意图与用户历史的结合可用于个性化 Agent，但研究核心仍是新闻推荐。

  <details>
  <summary>brief</summary>

  - **问题**：新闻快速更新且用户需求常无明确关键词，传统先检索流程难处理冷启动和隐含意图。
  - **方法**：从对话及画像生成层级语义标识，再匹配当前新闻池，并按历史可用性选择推理路径。
  - **价值**：以动态目录匹配保证推荐条目存在，同时利用用户记忆补足查询语义。
  - **局限**：条目存在不代表事实正确或推荐适合，效果依赖平台画像与语义索引体系。

  来源：<a href="https://aclanthology.org/2026.acl-industry.130">[1]</a> · <a href="https://arxiv.org/abs/2605.07613">[2]</a> · <a href="https://arxiv.org/pdf/2605.07613">[3]</a>
  核验：2026-10-13

  </details>


## 多模态检索

+ [RePair: Turning Retrieval Failures into Counterfactual Hard Pairs](<https://arxiv.org/abs/2608.29604>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2608.29604>)
  <br>2026-08-30 · 反事实增强 / 困难负例 / 记忆检索

  **[EMNLP 2026](<https://arxiv.org/abs/2608.29604>)** · **P1 重点** · 已核对正文
  以模型当前检索失败构造反事实训练对，可迁移到 Agent 记忆召回纠错。

  <details>
  <summary>brief</summary>

  - **问题**：通用数据增强不一定修复检索器当前的近邻语义混淆。
  - **方法**：双向挖掘并核验误召回，最小反事实编辑后组织3×3局部对比网格，保留原始全局损失。
  - **价值**：同预算消融支持失败定位与局部配对的贡献。
  - **局限**：仅单次模型快照挖掘，跨数据集迁移及融合式检索器未验证。

  来源：<a href="https://arxiv.org/abs/2608.29604">[1]</a> · <a href="https://arxiv.org/pdf/2608.29604v1">[2]</a>
  核验：2026-10-13

  </details>

+ [ObjEmbed: Towards Universal Multimodal Object Embeddings](<https://arxiv.org/abs/2602.01753>)<br>
  [![Star](https://img.shields.io/github/stars/WeChatCV/ObjEmbed.svg?style=social&label=Star)](<https://github.com/WeChatCV/ObjEmbed>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2602.01753>)
  <br>2026-02-02 · 多模态检索 / 对象表征 / 视觉记忆

  **[ICML 2026](<https://proceedings.mlr.press/v306/fu26p.html>)** · **P1 重点** · 摘要与引言
  对象语义与定位置信度联合编码适合构建可检索的视觉记忆。

  <details>
  <summary>brief</summary>

  - **问题**：全图嵌入难同时表达小对象语义与候选框定位可靠性。
  - **方法**：为每个候选区域并行生成语义和交并比嵌入，将语义匹配与定位质量联合打分。
  - **价值**：一次编码支持对象、局部及全局检索，可作为对象中心记忆的基础组件。
  - **局限**：依赖外部候选框，跨帧身份关联与长期状态维护仍需额外机制。

  来源：<a href="https://arxiv.org/abs/2602.01753">[1]</a> · <a href="https://arxiv.org/pdf/2602.01753">[2]</a> · <a href="https://github.com/WeChatCV/ObjEmbed">[3]</a> · <a href="https://proceedings.mlr.press/v306/fu26p.html">[4]</a>
  核验：2026-10-13

  </details>

+ [WAVE: Learning Unified &amp; Versatile Audio-Visual Embeddings with Multimodal LLM](<https://arxiv.org/abs/2509.21990>)<br>
  [![Star](https://img.shields.io/github/stars/TCL606/WAVE.svg?style=social&label=Star)](<https://github.com/TCL606/WAVE>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2509.21990>)
  <br>2025-09-26 · 多模态检索 / 视觉记忆 / 音视频表征

  **[ICLR 2026 Oral](<https://github.com/TCL606/WAVE>)** · **P1 重点** · 摘要与引言
  音视频统一且可按查询变化的嵌入适合多模态 Agent 记忆和交互内容检索。

  <details>
  <summary>brief</summary>

  - **问题**：静态图像嵌入难统一音频、视频及同步流，也难根据任务调整检索语义。
  - **方法**：在多模态语言模型上融合多层特征与双音频编码器，联合训练跨模态和多任务检索。
  - **价值**：提供可遵循提示的统一音视频表示，便于构建任务相关的记忆索引。
  - **局限**：语义检索表示不保证精确时间同步，尚未验证流式记忆更新与生成控制。

  来源：<a href="https://arxiv.org/abs/2509.21990">[1]</a> · <a href="https://arxiv.org/pdf/2509.21990">[2]</a> · <a href="https://github.com/TCL606/WAVE">[3]</a>
  核验：2026-10-13

  </details>

+ [From Saliency to Discriminability: Rank-Preserving Visual Token Pruning for VLM Rerankers](<https://arxiv.org/abs/2609.00667>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2609.00667>)
  <br>2026-09-01 · 多模态检索 / 推理效率 / 词元裁剪

  **[EMNLP 2026](<https://arxiv.org/abs/2609.00667>)** · **P2 选读** · 已核对正文
  细粒度视觉裁剪可借鉴到记忆检索效率，但主要验证静态图像重排序。

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
  <br>2026-08-30 · 多模态噪声 / 检索评测 / 鲁棒性

  **[Findings of EMNLP 2026](<https://arxiv.org/abs/2608.29607>)** · **P2 选读** · 已核对正文
  适合作为视觉记忆检索的鲁棒性参考，距生成和交互闭环较远。

  <details>
  <summary>brief</summary>

  - **问题**：拍照问答的图文噪声与粗粒度文本可能共同损害实体检索。
  - **方法**：固定目标及图库构造成对扰动，按图像排序一致性和分数方差自适应融合。
  - **价值**：揭示文本稀释视觉排序及联合扰动的非加性影响。
  - **局限**：1145查询且扰动为程序合成，不能替代真实上传分布评估。

  来源：<a href="https://arxiv.org/abs/2608.29607">[1]</a> · <a href="https://arxiv.org/pdf/2608.29607v1">[2]</a> · <a href="https://github.com/zrchen03/SnapBench">[3]</a>
  核验：2026-10-13

  </details>

+ [EviRank: Structured Relevance Evidence for Multimodal Image Re-ranking](<https://arxiv.org/abs/2608.20886>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2608.20886>)
  <br>2026-08-21 · 多模态检索 / 约束分解 / 证据排序

  **[EMNLP 2026](<https://enjundu.com/publication>)** · **P2 选读** · 已核对正文
  约束槽与证据排序可借鉴到检索记忆，但实验限于静态图像候选。

  <details>
  <summary>brief</summary>

  - **问题**：图像重排序易忽略组合查询中的细粒度约束。
  - **方法**：以六类语义槽表示必需、禁止及可忽略条件，先规则评分再局部列表比较。
  - **价值**：消融支持约束分解的作用，学生可脱离教师部署。
  - **局限**：效果受首轮候选覆盖限制，实验主要为英文静态图像。

  来源：<a href="https://arxiv.org/abs/2608.20886">[1]</a> · <a href="https://arxiv.org/pdf/2608.20886v1">[2]</a> · <a href="https://enjundu.com/publication">[3]</a>
  核验：2026-10-13

  </details>


## 评测与可靠性

+ [Can LLM-as-a-Judge Reliably Verify Rubrics in Agentic Scenarios?](<https://arxiv.org/abs/2606.29920>)<br>
  [![Star](https://img.shields.io/github/stars/THU-KEG/RuVerBench.svg?style=social&label=Star)](<https://github.com/THU-KEG/RuVerBench>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2606.29920>)
  <br>2026-06-29 · Agent评测 / 代码轨迹 / 奖励核验

  **[EMNLP 2026](<https://arxiv.org/abs/2606.29920>)** · **P1 重点** · 已核对正文
  细则可核验性评测适合约束 Agent 奖励设计，避免把裁判分数直接当能力。

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
  <br>2026-06-06 · 事实性评测 / 信息保持 / 摘要记忆

  **[EMNLP 2026](<https://arxiv.org/abs/2606.08000>)** · **P1 重点** · 已核对正文
  信息充分性与忠实性分开评测，可直接用于检验 Agent 摘要记忆是否损失关键证据。

  <details>
  <summary>brief</summary>

  - **问题**：整体偏好容易把摘要流畅度与信息充分性混为一谈。
  - **方法**：结合分维人工盲评、排除自评的模型裁判、外部事实核验与语言学分析。
  - **价值**：五数据集上人工摘要保有信息和忠实性优势。
  - **局限**：仅五个通用模型的零样本快照；外部事实正确不等于遵守仅据原文要求。

  来源：<a href="https://arxiv.org/abs/2606.08000">[1]</a> · <a href="https://arxiv.org/pdf/2606.08000v3">[2]</a>
  核验：2026-10-13

  </details>

+ [GenShield: Unified Detection and Artifact Correction for AI-Generated Images](<https://arxiv.org/abs/2605.16122>)<br>
  [![Star](https://img.shields.io/github/stars/zhipeixu/GenShield.svg?style=social&label=Star)](<https://github.com/zhipeixu/GenShield>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2605.16122>)
  <br>2026-05-15 · 生成Agent / 视觉纠错 / 闭环生成

  **[ICML 2026](<https://proceedings.mlr.press/v306/xu26cl.html>)** · **P1 重点** · 摘要与引言
  诊断、修复和停止条件构成生成 Agent 闭环，可借鉴到视频错误修正。

  <details>
  <summary>brief</summary>

  - **问题**：伪影检测通常只标出问题，依赖冻结修补器又可能引入新不一致。
  - **方法**：在共享多模态骨干上联合检测与生成专家，以课程学习训练先诊断再修复的多步过程。
  - **价值**：将缺陷解释转化为可执行修正，补充配对修复数据与停止机制。
  - **局限**：图像修复有效不代表跨帧修复稳定，反复编辑成本和语义漂移仍需关注。

  来源：<a href="https://arxiv.org/abs/2605.16122">[1]</a> · <a href="https://arxiv.org/pdf/2605.16122">[2]</a> · <a href="https://github.com/zhipeixu/GenShield">[3]</a> · <a href="https://proceedings.mlr.press/v306/xu26cl.html">[4]</a>
  核验：2026-10-13

  </details>

+ [Evaluating Generative Models via One-Dimensional Code Distributions](<https://arxiv.org/abs/2603.08064>)<br>
  [![Star](https://img.shields.io/github/stars/zexiJia/1d-Distance.svg?style=social&label=Star)](<https://github.com/zexiJia/1d-Distance>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2603.08064>)
  <br>2026-03-09 · 生成评估 / 离散视觉表征 / 质量指标

  **[CVPR 2026](<https://openaccess.thecvf.com/content/CVPR2026/supplemental/Jia_Evaluating_Generative_Models_CVPR_2026_supplemental.pdf>)** · **P1 重点** · 摘要与引言
  评估特征是否遗漏生成伪影是视频质量评价的基础问题，可先研究其图像版本。

  <details>
  <summary>brief</summary>

  - **问题**：识别特征的外观不变性会忽略生成图像的纹理与局部失真。
  - **方法**：在一维视觉码本中比较频率和共现统计，并以合成退化训练单图质量回归器。
  - **价值**：提供无需人工偏好标签的质量建模思路，并用多视觉形式数据检验跨域适应。
  - **局限**：仍依赖分词器与合成退化覆盖，未验证视频时序一致性。

  来源：<a href="https://arxiv.org/abs/2603.08064">[1]</a> · <a href="https://arxiv.org/pdf/2603.08064">[2]</a> · <a href="https://github.com/zexiJia/1d-Distance">[3]</a> · <a href="https://openaccess.thecvf.com/content/CVPR2026/supplemental/Jia_Evaluating_Generative_Models_CVPR_2026_supplemental.pdf">[4]</a>
  核验：2026-10-13

  </details>

+ [MR-ALIGN: Meta-Reasoning Informed Factuality Alignment for Large Reasoning Models](<https://arxiv.org/abs/2510.24794>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2510.24794>)
  <br>2025-10-27 · 事实性 / 元推理 / 过程对齐

  **[Findings of ACL 2026](<https://aclanthology.org/2026.findings-acl.204>)** · **P1 重点** · 摘要与引言
  推理中出现正确事实却最终丢弃，与 Agent 反思和记忆使用的可靠性密切相关。

  <details>
  <summary>brief</summary>

  - **问题**：模型推理时命中正确事实，仍可能在后续思考中将其否定并输出错误答案。
  - **方法**：标注原子思考片段及其状态转移，用转移感知的隐式奖励进行细粒度偏好对齐。
  - **价值**：把事实性问题定位到推理过程，而不仅是最终答案监督。
  - **局限**：无需外部验证器仍依赖片段标注，状态划分与跨任务因果有效性需检验。

  来源：<a href="https://aclanthology.org/2026.findings-acl.204">[1]</a> · <a href="https://arxiv.org/abs/2510.24794">[2]</a> · <a href="https://arxiv.org/pdf/2510.24794">[3]</a>
  核验：2026-10-13

  </details>

+ [FailureAtlas: Mapping the Failure Landscape of T2I Models via Active Exploration](<https://arxiv.org/abs/2509.21995>)<br>
  [![Star](https://img.shields.io/github/stars/cure-lab/FailureAtlas.svg?style=social&label=Star)](<https://github.com/cure-lab/FailureAtlas>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2509.21995>)
  <br>2025-09-26 · 主动探索 / 失败分析 / 生成评测

  **[CVPR 2026](<https://openaccess.thecvf.com/content/CVPR2026/html/Chen_FailureAtlas_Mapping_the_Failure_Landscape_of_T2I_Models_via_Active_CVPR_2026_paper.html>)** · **P1 重点** · 摘要与引言
  主动寻找最小失败组合，可用于视频生成核心缺陷诊断。

  <details>
  <summary>brief</summary>

  - **问题**：固定提示集只能显示失败，难定位触发问题的最小概念组合。
  - **方法**：在实体属性空间树搜索，以规则剪枝和失败预测器优先探索高价值分支。
  - **价值**：形成细粒度失败图谱并关联训练数据覆盖。
  - **局限**：依赖结构化概念空间及自动判别，相关性分析不能证明失败因果。

  来源：<a href="https://arxiv.org/abs/2509.21995">[1]</a> · <a href="https://arxiv.org/pdf/2509.21995">[2]</a> · <a href="https://github.com/cure-lab/FailureAtlas">[3]</a> · <a href="https://openaccess.thecvf.com/content/CVPR2026/html/Chen_FailureAtlas_Mapping_the_Failure_Landscape_of_T2I_Models_via_Active_CVPR_2026_paper.html">[4]</a>
  核验：2026-10-13

  </details>

+ [Sentient Agent as a Judge: Evaluating Higher-Order Social Cognition in Large Language Models](<https://arxiv.org/abs/2505.02847>)<br>
  [![Star](https://img.shields.io/github/stars/Tencent/DigitalHuman.svg?style=social&label=Star)](<https://github.com/Tencent/DigitalHuman>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2505.02847>)
  <br>2025-05-01 · Agent评测 / 交互Avatar / 社会认知

  **[Findings of ACL 2026](<https://aclanthology.org/2026.findings-acl.1905>)** · **P1 重点** · 摘要与引言
  交互 Avatar 需要对话层面的动态评价，可补充口型、画质之外的用户体验维度。

  <details>
  <summary>brief</summary>

  - **问题**：静态回答打分难反映多轮对话中用户情绪和隐含诉求如何变化。
  - **方法**：构建带角色、目标及隐藏意图的模拟用户，逐轮更新情绪与内心解释并输出轨迹分数。
  - **价值**：提供持续互动评价框架，帮助区分任务有用性与关系体验。
  - **局限**：情绪由语言模型模拟，相关性证据不能替代真人体验，也不证明模型具有感受。

  来源：<a href="https://aclanthology.org/2026.findings-acl.1905">[1]</a> · <a href="https://arxiv.org/abs/2505.02847">[2]</a> · <a href="https://arxiv.org/pdf/2505.02847">[3]</a> · <a href="https://github.com/Tencent/DigitalHuman/tree/main/SAGE">[4]</a>
  核验：2026-10-13

  </details>

+ [FactGuard: Leveraging Multi-Agent Systems to Generate Answerable and Unanswerable Questions for Enhanced Long-Context LLM Extraction](<https://arxiv.org/abs/2504.05607>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2504.05607>)
  <br>2025-04-08 · 拒答评测 / 证据可靠性 / 长文问答

  **arXiv 预印本（录用待核实）** · **P1 重点** · 已核对正文
  证据缺失与误导条件下的拒答评测，可用于检验 Agent 记忆检索的可信度。

  <details>
  <summary>brief</summary>

  - **问题**：长文问答常把相关但不足的证据误作可回答依据。
  - **方法**：筛选文本片段生成证据问答，再删除证据或改写错误前提，并检索复查冲突答案。
  - **价值**：区分缺失与误导证据，支持诊断拒答能力。
  - **局限**：本条据2025年公开初版；不能套用后续稿的11模型及71.62%结论。

  来源：<a href="https://arxiv.org/abs/2504.05607">[1]</a> · <a href="https://arxiv.org/pdf/2504.05607v1">[2]</a>
  核验：2026-10-13

  </details>

+ [Crossing the Reward Bridge: Expanding Reinforcement Learning with Verifiable Rewards Across Diverse Domains](<https://arxiv.org/abs/2503.23829>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2503.23829>)
  <br>2025-03-31 · 奖励模型 / 开放域推理 / 强化学习

  **[ACL 2026](<https://aclanthology.org/2026.acl-long.178>)** · **P1 重点** · 摘要与引言
  开放任务的验证奖励可用于 Agent 后训练，但要保留参考答案这一关键前提。

  <details>
  <summary>brief</summary>

  - **问题**：规则验证难覆盖自由形式答案，二元反馈也无法充分表达部分正确性。
  - **方法**：利用专家参考答案和教师判分蒸馏生成式验证器，以判定令牌概率提供软奖励。
  - **价值**：把可验证奖励扩展到多领域非结构化回答，降低专用评价模型成本。
  - **局限**：仍需要高质量参考与教师判断，不能等同于无参考开放环境中的可靠奖励。

  来源：<a href="https://aclanthology.org/2026.acl-long.178">[1]</a> · <a href="https://arxiv.org/abs/2503.23829">[2]</a> · <a href="https://arxiv.org/pdf/2503.23829">[3]</a>
  核验：2026-10-13

  </details>

+ [Identifying the Achilles’ Heel: An Iterative Method for Uncovering Factual Errors in Large Language Models](<https://arxiv.org/abs/2401.00761>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2401.00761>)
  <br>2024-01-01 · 主动测试 / 事实性评测 / 知识图谱

  **[Findings of ACL 2026](<https://aclanthology.org/2026.findings-acl.1714>)** · **P1 重点** · 摘要与引言
  面向模型弱点主动生成测试，可用于 Agent 知识与记忆检索的针对性诊断。

  <details>
  <summary>brief</summary>

  - **问题**：静态事实问答成本高且可能被训练污染，也难持续暴露模型薄弱知识区域。
  - **方法**：从知识图谱生成多类单跳和多跳问题，按历史错误自适应选择相近实体与关系。
  - **价值**：把失败反馈纳入评测采样，支持迭代定位知识缺口。
  - **局限**：结果受图谱正确性和答案匹配规则影响，动态出题并不消除全部知识污染。

  来源：<a href="https://aclanthology.org/2026.findings-acl.1714">[1]</a> · <a href="https://arxiv.org/abs/2401.00761">[2]</a> · <a href="https://arxiv.org/pdf/2401.00761">[3]</a>
  核验：2026-10-13

  </details>

+ [PointThinker: Point-Incentivized Parallel Thinking for Multimodal Large Language Model](<https://openaccess.thecvf.com/content/CVPR2026/papers/Hu_PointThinker_Point-Incentivized_Parallel_Thinking_for_Multimodal_Large_Language_Model_CVPR_2026_paper.pdf>)<br>
  [![Paper](https://img.shields.io/badge/Paper-b31b1b.svg)](<https://openaccess.thecvf.com/content/CVPR2026/papers/Hu_PointThinker_Point-Incentivized_Parallel_Thinking_for_Multimodal_Large_Language_Model_CVPR_2026_paper.pdf>)
  <br>日期待核实 · 多路径推理 / 视觉推理 / 过程奖励

  **[CVPR 2026](<https://openaccess.thecvf.com/content/CVPR2026/html/Hu_PointThinker_Point-Incentivized_Parallel_Thinking_for_Multimodal_Large_Language_Model_CVPR_2026_paper.html>)** · **P1 重点** · 摘要与引言
  对视觉推理分支进行细粒度归因，可借鉴到 Agent 的规划与过程奖励。

  <details>
  <summary>brief</summary>

  - **问题**：单一路径视觉推理容易遗漏关键线索，整段答案奖励难定位有效思考。
  - **方法**：先列出多个视觉关键点分别推理，再结合关键点与完整路径正确性分配分层策略奖励。
  - **价值**：让模型探索不同证据并区分有效推理分支，提供过程信用分配思路。
  - **局限**：关键点是语义线索而非像素坐标，额外推理成本与答案判定依赖仍存在。

  来源：<a href="https://openaccess.thecvf.com/content/CVPR2026/html/Hu_PointThinker_Point-Incentivized_Parallel_Thinking_for_Multimodal_Large_Language_Model_CVPR_2026_paper.html">[1]</a> · <a href="https://openaccess.thecvf.com/content/CVPR2026/papers/Hu_PointThinker_Point-Incentivized_Parallel_Thinking_for_Multimodal_Large_Language_Model_CVPR_2026_paper.pdf">[2]</a>
  核验：2026-10-13

  </details>

+ [Omni IIE Bench: Benchmarking the Practical Capabilities of Image Editing Models](<https://arxiv.org/abs/2603.16944>)<br>
  [![Star](https://img.shields.io/github/stars/Young-2000/OmniIIEBench.svg?style=social&label=Star)](<https://github.com/Young-2000/OmniIIEBench>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2603.16944>)
  <br>2026-03-16 · 一致性评测 / 图像编辑 / 多轮交互

  **[CVPR 2026](<https://openaccess.thecvf.com/content/CVPR2026/html/Yang_Omni_IIE_Bench_Benchmarking_the_Practical_Capabilities_of_Image_Editing_CVPR_2026_paper.html>)** · **P2 选读** · 摘要与引言
  多轮约束保持的评测设计可借鉴到交互视频，但主体是图像编辑。

  <details>
  <summary>brief</summary>

  - **问题**：混合任务平均分掩盖属性修改与实体替换之间的能力差异。
  - **方法**：在共享上下文中成对比较语义尺度，并设置长达多轮的连续编辑任务。
  - **价值**：把画质、区域保真与指令遵循分开诊断。
  - **局限**：合成样本和评测器仍有偏差，未直接覆盖视频时序一致性。

  来源：<a href="https://arxiv.org/abs/2603.16944">[1]</a> · <a href="https://arxiv.org/pdf/2603.16944">[2]</a> · <a href="https://github.com/Young-2000/OmniIIEBench">[3]</a> · <a href="https://openaccess.thecvf.com/content/CVPR2026/html/Yang_Omni_IIE_Bench_Benchmarking_the_Practical_Capabilities_of_Image_Editing_CVPR_2026_paper.html">[4]</a>
  核验：2026-10-13

  </details>

+ [DSH-Bench: A Difficulty- and Scenario-Aware Benchmark with Hierarchical Subject Taxonomy for Subject-Driven Text-to-Image Generation](<https://arxiv.org/abs/2603.08090>)<br>
  [![Star](https://img.shields.io/github/stars/sunriverhzy/DSH-Bench.svg?style=social&label=Star)](<https://github.com/sunriverhzy/DSH-Bench>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2603.08090>)
  <br>2026-03-09 · 主体一致性 / 指令遵循 / 生成评测

  **ECCV 2026（提供名单，待一手核实）** · **P2 选读** · 已核对正文
  分离主体保持与指令遵循有助于 Avatar 身份评测，但基准只覆盖静态单主体。

  <details>
  <summary>brief</summary>

  - **问题**：主体生成的总分掩盖复杂主体与不同指令场景的能力差异。
  - **方法**：按层级采样58类主体，交叉划分难度与场景，以人工评分及解释微调Qwen裁判。
  - **价值**：把主体保持、指令遵循和画质分开诊断，定位细节重建短板。
  - **局限**：聚焦单主体；身份保持与属性改写存在权衡，不能外推多主体交互。

  来源：<a href="https://arxiv.org/abs/2603.08090">[1]</a> · <a href="https://arxiv.org/pdf/2603.08090v3">[2]</a> · <a href="https://github.com/sunriverhzy/DSH-Bench">[3]</a>
  核验：2026-10-13

  </details>

+ [TranX-Adapter: Bridging Artifacts and Semantics within MLLMs for Robust AI-generated Image Detection](<https://arxiv.org/abs/2602.21716>)<br>
  [![Star](https://img.shields.io/github/stars/DreamMr/TranX-Adapter.svg?style=social&label=Star)](<https://github.com/DreamMr/TranX-Adapter>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2602.21716>)
  <br>2026-02-25 · 特征融合 / 生成内容检测 / 视觉伪影

  **[ICML 2026](<https://proceedings.mlr.press/v306/wang26cj.html>)** · **P2 选读** · 摘要与引言
  伪影与语义融合可辅助生成质量诊断，但真伪检测不是当前主研究目标。

  <details>
  <summary>brief</summary>

  - **问题**：纹理伪影特征相互过于相似，普通注意力融合容易稀释有效检测信号。
  - **方法**：以任务概率间距离构造最优传输，将伪影注入语义，再用交叉注意力反向融合。
  - **价值**：提供应对异质特征尺度与相似性差异的轻量适配思路。
  - **局限**：主要验证图像真伪分类，检测能力不直接等价于生成质量或视频一致性评估。

  来源：<a href="https://arxiv.org/abs/2602.21716">[1]</a> · <a href="https://arxiv.org/pdf/2602.21716">[2]</a> · <a href="https://github.com/DreamMr/TranX-Adapter">[3]</a> · <a href="https://proceedings.mlr.press/v306/wang26cj.html">[4]</a>
  核验：2026-10-13

  </details>

+ [ChartE3: A Comprehensive Benchmark for End-to-End Chart Editing](<https://arxiv.org/abs/2601.21694>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2601.21694>)
  <br>2026-01-29 · 图表编辑 / 生成评估 / 结构一致性

  **[ICML 2026](<https://proceedings.mlr.press/v306/li26fr.html>)** · **P2 选读** · 摘要与引言
  可参考结构化视觉编辑的评测设计，但与视频、世界模型和记忆主线较远。

  <details>
  <summary>brief</summary>

  - **问题**：图表编辑需要同时保持数字语义与视觉结构，代码生成评测难覆盖直接图像编辑。
  - **方法**：构建局部外观和全局数据变换任务，以配对图像、代码和指令建立评测集。
  - **价值**：把视觉相似与编辑正确性分开，揭示全局数据级修改的能力缺口。
  - **局限**：图像相似指标与模型裁判难充分保证数值正确性，任务范围集中于图表。

  来源：<a href="https://arxiv.org/abs/2601.21694">[1]</a> · <a href="https://arxiv.org/pdf/2601.21694">[2]</a> · <a href="https://proceedings.mlr.press/v306/li26fr.html">[3]</a>
  核验：2026-10-13

  </details>

+ [Too Good to be Bad: On the Failure of LLMs to Role-Play Villains](<https://arxiv.org/abs/2511.04962>)<br>
  [![Star](https://img.shields.io/github/stars/Tencent/DigitalHuman.svg?style=social&label=Star)](<https://github.com/Tencent/DigitalHuman>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2511.04962>)
  <br>2025-11-07 · 交互Avatar / 人物一致性 / 角色扮演

  **[Findings of ACL 2026](<https://aclanthology.org/2026.findings-acl.282>)** · **P2 选读** · 摘要与引言
  角色一致性对交互 Avatar 有价值，但论文侧重虚构人格评测而非实时生成。

  <details>
  <summary>brief</summary>

  - **问题**：语言模型扮演不同道德取向的虚构角色时，通用对话能力不一定对应角色忠实度。
  - **方法**：构建四级人格取向的平衡角色集，按特质检验模型是否保持人物动机与表达。
  - **价值**：为交互叙事中人物设定与模型默认行为的冲突提供诊断框架。
  - **局限**：评价依赖角色量表与裁判，对齐导致差异的解释不能代替受控因果实验。

  来源：<a href="https://aclanthology.org/2026.findings-acl.282">[1]</a> · <a href="https://arxiv.org/abs/2511.04962">[2]</a> · <a href="https://arxiv.org/pdf/2511.04962">[3]</a> · <a href="https://github.com/Tencent/DigitalHuman/tree/main/RolePlay_Villain">[4]</a>
  核验：2026-10-13

  </details>

+ [Social Welfare Function Leaderboard: On the Emergence of LLM Agents as the Welfare Dictator](<https://arxiv.org/abs/2510.01164>)<br>
  [![Star](https://img.shields.io/github/stars/tencent/digitalhuman.svg?style=social&label=Star)](<https://github.com/tencent/digitalhuman>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2510.01164>)
  <br>2025-10-01 · Agent评测 / 资源分配 / 长期决策

  **[Findings of ACL 2026](<https://aclanthology.org/2026.findings-acl.1919>)** · **P2 选读** · 摘要与引言
  长期资源分配可参考其历史反馈设计，但社会福利目标并非当前规划研究重点。

  <details>
  <summary>brief</summary>

  - **问题**：通用语言能力难反映持续分配资源时的效率与公平取舍。
  - **方法**：让模型依据历史表现向能力不同的代理分配任务，联合衡量回报与分配不平等。
  - **价值**：揭示评测目标和提示约束会如何改变长期决策策略。
  - **局限**：任务机会被简化为福利，特定合成指标与模拟环境不能代表真实社会分配。

  来源：<a href="https://aclanthology.org/2026.findings-acl.1919">[1]</a> · <a href="https://arxiv.org/abs/2510.01164">[2]</a> · <a href="https://arxiv.org/pdf/2510.01164">[3]</a> · <a href="https://github.com/tencent/digitalhuman/tree/main/SWF">[4]</a>
  核验：2026-10-13

  </details>

+ [A.S.E: A Repository-Level Benchmark for Evaluating Security in AI-Generated Code](<https://arxiv.org/abs/2508.18106>)<br>
  [![Star](https://img.shields.io/github/stars/Tencent/AICGSecEval.svg?style=social&label=Star)](<https://github.com/Tencent/AICGSecEval>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2508.18106>)
  <br>2025-08-25 · 仓库级评测 / 代码Agent / 代码安全

  **[Findings of ACL 2026](<https://aclanthology.org/2026.findings-acl.1569>)** · **P2 选读** · 摘要与引言
  可补充代码 Agent 的任务评测，但与规划和记忆机制研究的联系较间接。

  <details>
  <summary>brief</summary>

  - **问题**：片段级代码测试难覆盖真实仓库中的上下文依赖和安全漏洞。
  - **方法**：从已知漏洞修复构造跨文件补全任务，以变异样本和专用静态规则评测生成结果。
  - **价值**：将功能、稳定性和漏洞风险联合纳入可重复的仓库级评测。
  - **局限**：覆盖有限漏洞类型，静态规则通过并不意味着不存在其他缺陷。

  来源：<a href="https://aclanthology.org/2026.findings-acl.1569">[1]</a> · <a href="https://arxiv.org/abs/2508.18106">[2]</a> · <a href="https://arxiv.org/pdf/2508.18106">[3]</a> · <a href="https://github.com/Tencent/AICGSecEval">[4]</a>
  核验：2026-10-13

  </details>

+ [RedEdit: Agentic Red-Teaming of Image Safety Classifiers via MCTS-Guided Photo-Editing](<https://arxiv.org/abs/2606.06140>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2606.06140>)
  <br>2026-06-04 · 图像编辑 / 安全评测 / 树搜索

  **arXiv 预印本（录用待核实）** · **P3 暂缓** · 已核对正文
  主要评估图像审核稳健性；当前研究可暂缓，需做生成安全评测时再读。

  <details>
  <summary>brief</summary>

  - **问题**：图像审核器对常见照片编辑的稳健性缺少系统评测。
  - **方法**：用视觉模型提议与树搜索组织编辑序列，同时核验检测结果和内容保留。
  - **价值**：为审核防御提供跨检测器失效诊断。
  - **局限**：76.2%来自原本被拦截的164张中125张，非全部777张；编辑深度不等于查询次数。

  来源：<a href="https://arxiv.org/abs/2606.06140">[1]</a> · <a href="https://arxiv.org/pdf/2606.06140v1">[2]</a>
  核验：2026-10-13

  </details>

+ [Purify then Guide: Rethinking Domain Generalization for Multimodal Face Anti-Spoofing](<https://arxiv.org/abs/2505.09484>)<br>
  [![Star](https://img.shields.io/github/stars/murInJ/MMDA.svg?style=social&label=Star)](<https://github.com/murInJ/MMDA>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2505.09484>)
  <br>2025-05-14 · 人脸反欺骗 / 域泛化 / 多模态对齐

  **[ECCV 2026](<https://arxiv.org/abs/2505.09484>)** · **P3 暂缓** · 已核对正文
  聚焦人脸反欺骗的跨域识别；与 Avatar 生成质量和延迟的直接联系较弱。

  <details>
  <summary>brief</summary>

  - **问题**：直接对齐多模态特征会同时对齐伪造线索和域偏差。
  - **方法**：以同域异样本差分抑制共有噪声，再软对齐多提示语义子空间，并用U形适配保留CLIP结构。
  - **价值**：将去噪、语义引导与任务适配分开处理，兼顾缺失模态场景。
  - **局限**：依赖同域共享偏差的建模假设；基准收益不等于开放环境安全保证。

  来源：<a href="https://arxiv.org/abs/2505.09484">[1]</a> · <a href="https://arxiv.org/pdf/2505.09484v2">[2]</a> · <a href="https://github.com/murInJ/MMDA">[3]</a>
  核验：2026-10-13

  </details>


## 训练与推理效率

+ [HyQuant: Hybrid-Precision Quantization for LLM Attention](<https://arxiv.org/abs/2608.27875>)<br>
  [![Star](https://img.shields.io/github/stars/jerrysfls/HyQuant.svg?style=social&label=Star)](<https://github.com/jerrysfls/HyQuant>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2608.27875>)
  <br>2026-08-28 · KV量化 / 部署效率 / 长上下文

  **[EMNLP 2026](<https://arxiv.org/abs/2608.27875>)** · **P1 重点** · 已核对正文
  选择性高精度 KV 为长上下文部署提供工程参考，需要区分内核和端到端收益。

  <details>
  <summary>brief</summary>

  - **问题**：均匀低比特量化会放大高注意力位置的误差。
  - **方法**：保留高列注意力词元和局部窗口为高精度，将其余KV量化并融合反量化计算。
  - **价值**：在所测模型上接近全精度，减轻长上下文显存压力。
  - **局限**：32K内核加速3.58倍但端到端仅1.17倍，依赖H100设置。

  来源：<a href="https://arxiv.org/abs/2608.27875">[1]</a> · <a href="https://arxiv.org/pdf/2608.27875v3">[2]</a> · <a href="https://github.com/jerrysfls/HyQuant">[3]</a>
  核验：2026-10-13

  </details>

+ [Hybrid Policy Distillation for LLMs](<https://arxiv.org/abs/2604.20244>)<br>
  [![Star](https://img.shields.io/github/stars/zwhong714/Hybrid-Policy-Distillation.svg?style=social&label=Star)](<https://github.com/zwhong714/Hybrid-Policy-Distillation>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2604.20244>)
  <br>2026-04-22 · 推理加速 / 策略蒸馏 / 语言模型

  **[ICML 2026](<https://proceedings.mlr.press/v306/zhu26av.html>)** · **P1 重点** · 摘要与引言
  适合低成本压缩 Agent 推理能力，关注离线与学生采样之间的分布差异。

  <details>
  <summary>brief</summary>

  - **问题**：语言模型蒸馏中散度方向、数据来源和优化方式相互耦合，影响稳定性与成本。
  - **方法**：统一为逐词加权似然，结合离线专家令牌与轻量学生采样，平衡正反向散度信号。
  - **价值**：提供接近监督微调成本的混合策略蒸馏路径。
  - **局限**：需要教师概率信息，数学与对话收益尚不能代表交互规划能力得到保留。

  来源：<a href="https://arxiv.org/abs/2604.20244">[1]</a> · <a href="https://arxiv.org/pdf/2604.20244">[2]</a> · <a href="https://github.com/zwhong714/Hybrid-Policy-Distillation">[3]</a> · <a href="https://proceedings.mlr.press/v306/zhu26av.html">[4]</a>
  核验：2026-10-13

  </details>

+ [Stem: Rethinking Causal Information Flow in Sparse Attention](<https://arxiv.org/abs/2603.06274>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2603.06274>)
  <br>2026-03-06 · 推理加速 / 稀疏注意力 / 长上下文

  **[ICML 2026](<https://proceedings.mlr.press/v306/niu26b.html>)** · **P1 重点** · 摘要与引言
  长上下文首词延迟直接影响交互 Agent，稀疏预算分配比单纯压缩记忆更贴近部署。

  <details>
  <summary>brief</summary>

  - **问题**：统一稀疏预算忽略因果注意力中早期令牌的跨层影响，容易放大信息损失。
  - **方法**：为前部位置分配更多预算，并结合值向量估计输出贡献来筛选注意力块。
  - **价值**：在无需训练的条件下降低预填充成本，可支持较长历史的交互推理。
  - **局限**：面向语言模型预填充，不能直接视为语义记忆管理或视频模型加速结论。

  来源：<a href="https://arxiv.org/abs/2603.06274">[1]</a> · <a href="https://arxiv.org/pdf/2603.06274">[2]</a> · <a href="https://proceedings.mlr.press/v306/niu26b.html">[3]</a>
  核验：2026-10-13

  </details>

+ [SED-SFT: Selectively Encouraging Diversity in Supervised Fine-Tuning](<https://arxiv.org/abs/2602.07464>)<br>
  [![Star](https://img.shields.io/github/stars/pppa2019/SED-SFT.svg?style=social&label=Star)](<https://github.com/pppa2019/SED-SFT>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2602.07464>)
  <br>2026-02-07 · 强化学习 / 探索多样性 / 监督微调

  **[ACL 2026](<https://aclanthology.org/2026.acl-short.54>)** · **P1 重点** · 摘要与引言
  Agent 后训练需要保留探索空间，可作为监督微调到强化学习衔接的简洁基线。

  <details>
  <summary>brief</summary>

  - **问题**：交叉熵微调会收缩输出分布，妨碍后续强化学习探索，而统一增熵又损害正确性。
  - **方法**：依据令牌可探索空间选择性施加熵正则，并屏蔽不宜增加多样性的位置。
  - **价值**：把探索能力保护前移到监督阶段，减少后训练的模式塌缩。
  - **局限**：证据集中于数学推理，交互轨迹和工具调用的有效多样性还需重新定义。

  来源：<a href="https://aclanthology.org/2026.acl-short.54">[1]</a> · <a href="https://arxiv.org/abs/2602.07464">[2]</a> · <a href="https://arxiv.org/pdf/2602.07464">[3]</a> · <a href="https://github.com/pppa2019/SED-SFT">[4]</a>
  核验：2026-10-13

  </details>

+ [Lil: Less is Less When Applying Post-Training Sparse-Attention Algorithms in Long-Decode Stage](<https://arxiv.org/abs/2601.03043>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2601.03043>)
  <br>2026-01-06 · 提前停止 / 稀疏注意力 / 长推理

  **[Findings of ACL 2026](<https://aclanthology.org/2026.findings-acl.91>)** · **P1 重点** · 摘要与引言
  提醒实时 Agent 应评估整轮延迟与推理长度，适合和稀疏注意力方案配套阅读。

  <details>
  <summary>brief</summary>

  - **问题**：解码稀疏化虽减少单步计算，却可能因信息丢失诱发重复推理和更长输出。
  - **方法**：分析压缩率与信息增益关系，在输出信息不再增长时触发提前停止。
  - **价值**：把加速评价从单步速度扩展到端到端成本，揭示记忆压缩的隐藏代价。
  - **局限**：针对后训练稀疏化而非所有稀疏架构，停止阈值仍存在准确率权衡。

  来源：<a href="https://aclanthology.org/2026.findings-acl.91">[1]</a> · <a href="https://arxiv.org/abs/2601.03043">[2]</a> · <a href="https://arxiv.org/pdf/2601.03043">[3]</a>
  核验：2026-10-13

  </details>

+ [Find Your Optimal Teacher: Personalized Data Synthesis via Router-Guided Multi-Teacher Distillation](<https://arxiv.org/abs/2510.10925>)<br>
  [![Star](https://img.shields.io/github/stars/rattlesnakey/PerSyn.svg?style=social&label=Star)](<https://github.com/rattlesnakey/PerSyn>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2510.10925>)
  <br>2025-10-13 · 小模型 / 教师路由 / 数据蒸馏

  **[ACL 2026](<https://aclanthology.org/2026.acl-long.666>)** · **P1 重点** · 摘要与引言
  面向小型交互 Agent 的数据蒸馏有价值，可与推理时动态路由区分阅读。

  <details>
  <summary>brief</summary>

  - **问题**：更强教师的复杂回答未必适合学生，全部教师先生成再筛选又浪费成本。
  - **方法**：根据回答质量与学生可学习性训练查询路由器，先分配教师再生成蒸馏样本。
  - **价值**：将学生能力纳入数据选择，降低多教师合成成本。
  - **局限**：路由器本身需要配对教师数据，学生和任务变化后可能需要重新训练。

  来源：<a href="https://aclanthology.org/2026.acl-long.666">[1]</a> · <a href="https://arxiv.org/abs/2510.10925">[2]</a> · <a href="https://arxiv.org/pdf/2510.10925">[3]</a> · <a href="https://github.com/rattlesnakey/PerSyn">[4]</a>
  核验：2026-10-13

  </details>

+ [SpecExit: Accelerating Large Reasoning Model via Speculative Exit](<https://arxiv.org/abs/2509.24248>)<br>
  [![Star](https://img.shields.io/github/stars/Tencent/AngelSlim.svg?style=social&label=Star)](<https://github.com/Tencent/AngelSlim>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2509.24248>)
  <br>2025-09-29 · 推测解码 / 推理加速 / 提前退出

  **[ICML 2026](<https://proceedings.mlr.press/v306/yang26a.html>)** · **P1 重点** · 摘要与引言
  实时 Agent 要减少整轮等待，可结合推测解码与何时停止思考一起读。

  <details>
  <summary>brief</summary>

  - **问题**：长推理常包含冗余步骤，而额外探测是否结束又会抵消延迟收益。
  - **方法**：扩展轻量草稿模型，从隐藏状态同时预测未来令牌与推理结束信号。
  - **价值**：把逐词加速和缩短推理链统一到同一解码流程。
  - **局限**：提前停止涉及准确率权衡，其任务内效果不能保证复杂交互规划不会过早终止。

  来源：<a href="https://arxiv.org/abs/2509.24248">[1]</a> · <a href="https://arxiv.org/pdf/2509.24248">[2]</a> · <a href="https://github.com/Tencent/AngelSlim">[3]</a> · <a href="https://proceedings.mlr.press/v306/yang26a.html">[4]</a>
  核验：2026-10-13

  </details>

+ [WeTok: Powerful Discrete Tokenization for High-Fidelity Visual Reconstruction](<https://arxiv.org/abs/2508.05599>)<br>
  [![Star](https://img.shields.io/github/stars/zhuangshaobin/WeTok.svg?style=social&label=Star)](<https://github.com/zhuangshaobin/WeTok>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2508.05599>)
  <br>2025-08-07 · 生成压缩 / 离散表征 / 视觉分词器

  **[ICLR 2026](<https://proceedings.iclr.cc/paper_files/paper/2026/hash/0b2a58f2b5943b9c356f10db32073275-Abstract-Conference.html>)** · **P1 重点** · 摘要与引言
  生成底座的压缩与细节保真影响视频成本，可作离散视觉表示基础阅读。

  <details>
  <summary>brief</summary>

  - **问题**：扩大离散码本受训练开销限制，确定性解码又难在高压缩率下恢复细节。
  - **方法**：分组执行无查表量化，并引入额外噪声驱动生成式解码器建模条件分布。
  - **价值**：同时探索码本扩展和解码表达力，为高效视觉生成提供组件。
  - **局限**：图像重建分数不等于细节忠实还原，随机补全在视频中可能引入闪烁。

  来源：<a href="https://arxiv.org/abs/2508.05599">[1]</a> · <a href="https://arxiv.org/pdf/2508.05599">[2]</a> · <a href="https://github.com/zhuangshaobin/WeTok">[3]</a> · <a href="https://proceedings.iclr.cc/paper_files/paper/2026/hash/0b2a58f2b5943b9c356f10db32073275-Abstract-Conference.html">[4]</a>
  核验：2026-10-13

  </details>

+ [Investigating Cross-Modal Skill Injection: Scenarios, Methods, and Hyperparameters](<https://arxiv.org/abs/2605.19523>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2605.19523>)
  <br>2026-05-19 · 模型合并 / 能力注入 / 跨模态迁移

  **[ACL 2026](<https://aclanthology.org/2026.acl-long.571>)** · **P2 选读** · 摘要与引言
  为多模态 Agent 迁移语言技能提供低成本路径，但不是外部技能记忆或工具注入。

  <details>
  <summary>brief</summary>

  - **问题**：专用多模态数据昂贵，语言专家能力能否通过权重合并迁移缺少系统规律。
  - **方法**：比较任务场景、合并方法与超参数搜索，分析语言、指令和数学能力的迁移差异。
  - **价值**：提供何时值得尝试免重训技能迁移的经验依据。
  - **局限**：数学迁移较困难，效果依赖模型兼容性和调参，不能保证新技能自然组合。

  来源：<a href="https://aclanthology.org/2026.acl-long.571">[1]</a> · <a href="https://arxiv.org/abs/2605.19523">[2]</a> · <a href="https://arxiv.org/pdf/2605.19523">[3]</a>
  核验：2026-10-13

  </details>

+ [KDFlow: A User-Friendly and Efficient Knowledge Distillation Framework for Large Language Models](<https://arxiv.org/abs/2603.01875>)<br>
  [![Star](https://img.shields.io/github/stars/songmzhang/KDFlow.svg?style=social&label=Star)](<https://github.com/songmzhang/KDFlow>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2603.01875>)
  <br>2026-03-02 · 蒸馏系统 / 训练效率 / 通信优化

  **[EMNLP 2026 System Demonstrations](<https://github.com/songmzhang/KDFlow>)** · **P2 选读** · 已核对正文
  教师与学生后端解耦可借鉴蒸馏工程，论文主线是语言模型分布蒸馏。

  <details>
  <summary>brief</summary>

  - **问题**：教师推理与学生训练共用后端低效，全词表输出传输昂贵。
  - **方法**：教师由SGLang执行，仅传末层隐状态，在FSDP2学生侧重算完整输出分布。
  - **价值**：保持蒸馏损失并降低通信，离线实验加速1.44至6.36倍。
  - **局限**：上限采用FP8教师；超64卡扩展与异步训练尚未验证。

  来源：<a href="https://arxiv.org/abs/2603.01875">[1]</a> · <a href="https://arxiv.org/pdf/2603.01875v4">[2]</a> · <a href="https://github.com/songmzhang/KDFlow">[3]</a>
  核验：2026-10-13

  </details>

+ [CoMoL: Efficient Mixture of LoRA Experts via Dynamic Core Space Merging](<https://arxiv.org/abs/2603.00573>)<br>
  [![Star](https://img.shields.io/github/stars/DCDmllm/CoMoL.svg?style=social&label=Star)](<https://github.com/DCDmllm/CoMoL>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2603.00573>)
  <br>2026-02-28 · 低秩适配 / 参数高效微调 / 混合专家

  **[Findings of ACL 2026](<https://aclanthology.org/2026.findings-acl.811>)** · **P2 选读** · 摘要与引言
  可用于低成本领域适配，但与外部记忆或任务级多 Agent 分工不同。

  <details>
  <summary>brief</summary>

  - **问题**：多个完整低秩专家会增加参数，样本级路由又限制细粒度适配。
  - **方法**：将专家存于共享低秩空间的小核心矩阵，按令牌选择并软合并，同时压缩路由器。
  - **价值**：在接近单个低秩适配器参数量下保留专家差异。
  - **局限**：共享子空间可能限制容量，语言任务收益尚不能保证视频生成或长期记忆效果。

  来源：<a href="https://aclanthology.org/2026.findings-acl.811">[1]</a> · <a href="https://arxiv.org/abs/2603.00573">[2]</a> · <a href="https://arxiv.org/pdf/2603.00573">[3]</a> · <a href="https://github.com/DCDmllm/CoMoL">[4]</a>
  核验：2026-10-13

  </details>

+ [Sherry: Hardware-Efficient 1.25-Bit Ternary Quantization via Fine-grained Sparsification](<https://arxiv.org/abs/2601.07892>)<br>
  [![Star](https://img.shields.io/github/stars/Tencent/AngelSlim.svg?style=social&label=Star)](<https://github.com/Tencent/AngelSlim>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2601.07892>)
  <br>2026-01-12 · 模型量化 / 硬件效率 / 端侧推理

  **[ACL 2026](<https://aclanthology.org/2026.acl-long.513>)** · **P2 选读** · 摘要与引言
  若研究端侧低延迟 Agent 可提高优先级，当前更偏硬件与量化实现。

  <details>
  <summary>brief</summary>

  - **问题**：三值权重的紧凑存储与硬件向量宽度不匹配，理论位数优势难转化为速度。
  - **方法**：每四权重保留三个非零值，以五位打包，并用退火残差机制避免训练中权重聚集。
  - **价值**：从存储格式和训练共同设计端侧压缩，强调真实运行收益。
  - **局限**：速度收益依赖处理器与内核，不能按位宽比例推断整体 Agent 延迟。

  来源：<a href="https://aclanthology.org/2026.acl-long.513">[1]</a> · <a href="https://arxiv.org/abs/2601.07892">[2]</a> · <a href="https://arxiv.org/pdf/2601.07892">[3]</a> · <a href="https://github.com/Tencent/AngelSlim">[4]</a>
  核验：2026-10-13

  </details>

+ [Union-of-Experts: Neurons in Mixture-of-Experts are Secretly Routers](<https://aclanthology.org/2026.acl-long.1675.pdf>)<br>
  [![Star](https://img.shields.io/github/stars/ericshwu/Union-of-Experts.svg?style=social&label=Star)](<https://github.com/ericshwu/Union-of-Experts>) [![Paper](https://img.shields.io/badge/Paper-b31b1b.svg)](<https://aclanthology.org/2026.acl-long.1675.pdf>)
  <br>日期待核实 · 参数效率 / 混合专家 / 路由机制

  **[ACL 2026](<https://aclanthology.org/2026.acl-long.1675>)** · **P2 选读** · 摘要与引言
  属于底座架构研究，与 Agent 的任务规划和外部记忆并非同一层面。

  <details>
  <summary>brief</summary>

  - **问题**：独立路由器不了解专家内部能力，全部执行专家再选择又代价过高。
  - **方法**：用各专家少量神经元预测激活强度，自主选择令牌，并汇总路由输出形成虚拟共享专家。
  - **价值**：把路由与专家能力联系起来，同时复用路由计算改善参数效率。
  - **局限**：结论来自有限模型规模预训练，不直接解决多 Agent 的任务分配或规划。

  来源：<a href="https://aclanthology.org/2026.acl-long.1675">[1]</a> · <a href="https://aclanthology.org/2026.acl-long.1675.pdf">[2]</a> · <a href="https://github.com/ericshwu/Union-of-Experts">[3]</a>
  核验：2026-10-13

  </details>

+ [Your Inference Request Will Become a Black Box: Confidential Inference for Cloud-based Large Language Models](<https://arxiv.org/abs/2603.00196>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2603.00196>)
  <br>2026-02-27 · 云端部署 / 机密推理 / 隐私计算

  **[ACL 2026](<https://aclanthology.org/2026.acl-long.4>)** · **P3 暂缓** · 摘要与引言
  更适合隐私推理系统方向，当前与视频生成、规划及记忆算法联系较弱。

  <details>
  <summary>brief</summary>

  - **问题**：云端语言模型推理难同时保护输入输出、模型权重并维持质量与效率。
  - **方法**：将敏感操作放入客户控制的机密虚拟机，权重计算经可逆掩码协议外包给云端设备。
  - **价值**：探索在输出不变约束下划分可信边界和计算负载。
  - **局限**：安全结论依赖威胁模型与可信硬件，攻击实验不能证明对所有信息泄漏均有效。

  来源：<a href="https://aclanthology.org/2026.acl-long.4">[1]</a> · <a href="https://arxiv.org/abs/2603.00196">[2]</a> · <a href="https://arxiv.org/pdf/2603.00196">[3]</a>
  核验：2026-10-13

  </details>


## 多模态架构与综述

+ [A Survey on Rubric-Guided Reinforcement Learning for Language Models](<https://arxiv.org/abs/2608.27505>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2608.27505>)
  <br>2026-08-27 · 奖励审计 / 奖励设计 / 强化学习 / 综述

  **[Findings of EMNLP 2026](<https://arxiv.org/abs/2608.27505>)** · **P1 重点** · 已核对正文
  奖励细则与语义漂移框架可用于审计视频后训练和 Agent 过程奖励。

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
  <br>2026-05-25 · 原生多模态 / 架构综述 / 流式交互

  **arXiv 预印本（录用待核实）** · **P1 重点** · 已核对正文
  原生多模态架构与响应时机评测，为实时音视频 Avatar 系统设计建立背景。

  <details>
  <summary>brief</summary>

  - **问题**：原生多模态的融合深度与输入输出能力缺少统一描述。
  - **方法**：交叉梳理中早期融合与三类模态流，比较离散统一和保留模态特性的路线。
  - **价值**：串联数据配比、训练、流式部署，并提出质量与响应时机联合评测。
  - **局限**：属分类与路线展望，未以受控实验确立早期融合的普遍优势。

  来源：<a href="https://arxiv.org/abs/2605.25343">[1]</a> · <a href="https://arxiv.org/pdf/2605.25343v1">[2]</a> · <a href="https://nmm-roadmap.github.io/">[3]</a>
  核验：2026-10-13

  </details>

+ [WeMMU: Enhanced Bridging of Vision-Language Models and Diffusion Models via Noisy Query Tokens](<https://arxiv.org/abs/2512.02536>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2512.02536>)
  <br>2025-12-02 · 任务泛化 / 生成表征 / 统一多模态

  **[CVPR 2026](<https://openaccess.thecvf.com/content/CVPR2026/html/Yang_WeMMU_Enhanced_Bridging_of_Vision-Language_Models_and_Diffusion_Models_via_CVPR_2026_paper.html>)** · **P1 重点** · 摘要与引言
  随机查询的跨任务泛化机制值得用于统一视频理解与生成，但尚未直接验证视频。

  <details>
  <summary>brief</summary>

  - **问题**：固定查询桥接理解与生成时，模型容易记忆训练任务而失去新任务能力。
  - **方法**：用带噪查询替代固定查询，并让视觉语言模型融合低层视觉特征后对齐生成专家。
  - **价值**：为统一理解与生成模型减少任务捷径提供可迁移思路。
  - **局限**：证据主要来自图像任务，能否支持长视频状态与动态建模仍待验证。

  来源：<a href="https://arxiv.org/abs/2512.02536">[1]</a> · <a href="https://arxiv.org/pdf/2512.02536">[2]</a> · <a href="https://openaccess.thecvf.com/content/CVPR2026/html/Yang_WeMMU_Enhanced_Bridging_of_Vision-Language_Models_and_Diffusion_Models_via_CVPR_2026_paper.html">[3]</a>
  核验：2026-10-13

  </details>

+ [Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models](<https://arxiv.org/abs/2601.14004>)<br>
  [![Star](https://img.shields.io/github/stars/rattlesnakey/Awesome-Actionable-MI-Survey.svg?style=social&label=Star)](<https://github.com/rattlesnakey/Awesome-Actionable-MI-Survey>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2601.14004>)
  <br>2026-01-20 · 机制可解释性 / 模型干预 / 综述

  **[Findings of ACL 2026](<https://aclanthology.org/2026.findings-acl.502>)** · **P2 选读** · 摘要与引言
  适合作为定位与干预模型机制的工具索引，当前优先于泛读全篇的是查阅相关方法。

  <details>
  <summary>brief</summary>

  - **问题**：解释性研究常停留在观察，缺少从诊断到可验证模型改进的操作框架。
  - **方法**：按神经元、注意力头等对象整理定位与干预方法，并映射到能力、对齐和效率应用。
  - **价值**：为研究推理及记忆故障提供方法选择与因果验证的参考路线。
  - **局限**：属于综述而非统一实证，局部可控特征未必能跨任务稳定改善模型。

  来源：<a href="https://aclanthology.org/2026.findings-acl.502">[1]</a> · <a href="https://arxiv.org/abs/2601.14004">[2]</a> · <a href="https://arxiv.org/pdf/2601.14004">[3]</a> · <a href="https://github.com/rattlesnakey/Awesome-Actionable-MI-Survey">[4]</a>
  核验：2026-10-13

  </details>

+ [Bee: A High-Quality Corpus and Full-Stack Suite to Unlock Advanced Fully Open MLLMs](<https://arxiv.org/abs/2510.13795>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2510.13795>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://open-bee.github.io/>)
  <br>2025-10-15 · 多模态数据 / 思维链 / 数据清洗

  **[ICLR 2026](<https://proceedings.iclr.cc/paper_files/paper/2026/hash/171291d8fed723c6dfc76330aa827ff8-Abstract-Conference.html>)** · **P2 选读** · 摘要与引言
  训练多模态 Agent 底座时值得参考数据流程，当前与记忆和视频主线间接相关。

  <details>
  <summary>brief</summary>

  - **问题**：开放多模态训练数据含噪且缺少复杂推理样本，数据整理流程也难复用。
  - **方法**：公开清洗管线，按指令复杂度补充长短思维链，并训练模型验证各阶段收益。
  - **价值**：可借鉴可持续迭代的数据配方，而不局限于下载静态样本集合。
  - **局限**：模型生成的推理监督仍可能带偏差，非流式交互与长期记忆数据方案。

  来源：<a href="https://arxiv.org/abs/2510.13795">[1]</a> · <a href="https://arxiv.org/pdf/2510.13795">[2]</a> · <a href="https://open-bee.github.io/">[3]</a> · <a href="https://proceedings.iclr.cc/paper_files/paper/2026/hash/171291d8fed723c6dfc76330aa827ff8-Abstract-Conference.html">[4]</a>
  核验：2026-10-13

  </details>


## 三维生成与重建

+ [OmniX: Any-view and Any-time 4D Reconstruction via Feed-forward Trajectory Fields](<https://arxiv.org/abs/2607.10840>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2607.10840>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://omnix4d.github.io/>)
  <br>2026-07-12 · 几何监督 / 四维重建 / 点轨迹

  **[ECCV 2026](<https://arxiv.org/abs/2607.10840>)** · **P1 重点** · 已核对正文
  跨视角逐像素三维轨迹可提供世界模型的几何监督与动态一致性评测。

  <details>
  <summary>brief</summary>

  - **问题**：静态几何与动态对应混合建模，妨碍大幅视角变化下的四维重建。
  - **方法**：用少量动态词元与稀疏时空注意力分离运动，再以可变形采样头输出逐像素轨迹。
  - **价值**：一次前馈整合跨视角和时刻观测，配套UE5几何标注数据。
  - **局限**：方法利用运动稀疏低秩假设；并非直接生成可渲染的动态资产。

  来源：<a href="https://arxiv.org/abs/2607.10840">[1]</a> · <a href="https://arxiv.org/pdf/2607.10840v1">[2]</a> · <a href="https://omnix4d.github.io/">[3]</a>
  核验：2026-10-13

  </details>

+ [WorldMirror: Universal 3D World Reconstruction with Any-Prior Prompting](<https://arxiv.org/abs/2510.10726>)<br>
  [![Star](https://img.shields.io/github/stars/Tencent-Hunyuan/HunyuanWorld-Mirror.svg?style=social&label=Star)](<https://github.com/Tencent-Hunyuan/HunyuanWorld-Mirror>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2510.10726>)
  <br>2025-10-12 · 三维重建 / 世界模型基础 / 几何先验

  **[ICML 2026](<https://proceedings.mlr.press/v306/liu26cw.html>)** · **P1 重点** · 摘要与引言
  可为世界模型提供几何状态和约束，但本身解决的是重建而非未来动力学。

  <details>
  <summary>brief</summary>

  - **问题**：图像重建模型通常无法统一利用相机、深度等可用先验，也难覆盖多种几何输出。
  - **方法**：将多模态先验统一编码为令牌，通过多头空间预测和分阶段训练协调几何任务。
  - **价值**：为场景状态初始化与几何一致性约束提供可复用底座。
  - **局限**：前馈几何重建不等于动态预测，交互中的状态更新与因果响应尚未验证。

  来源：<a href="https://arxiv.org/abs/2510.10726">[1]</a> · <a href="https://arxiv.org/pdf/2510.10726">[2]</a> · <a href="https://github.com/Tencent-Hunyuan/HunyuanWorld-Mirror">[3]</a> · <a href="https://proceedings.mlr.press/v306/liu26cw.html">[4]</a>
  核验：2026-10-13

  </details>

+ [EditVerse3D: High-Quality 3D Object Editing with Region-Aware Learning](<https://arxiv.org/abs/2607.07187>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2607.07187>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://editverse3d.github.io/>)
  <br>2026-07-08 · 三维编辑 / 区域学习 / 资产生成

  **[ECCV 2026](<https://arxiv.org/abs/2607.07187>)** · **P2 选读** · 已核对正文
  局部区域学习有助于可编辑资产，但与实时生成和规划主线联系较弱。

  <details>
  <summary>brief</summary>

  - **问题**：精确掩码与多视图编辑流程增加三维局部修改的操作成本。
  - **方法**：基于TRELLIS输入粗三维框和参考图，自适应加权难学区域，以移除再恢复部件构造训练对。
  - **价值**：将编辑区学习与保留区约束结合，降低精细标注要求。
  - **局限**：训练以添加编辑为主；仍需输入三维对象、区域框和目标图。

  来源：<a href="https://arxiv.org/abs/2607.07187">[1]</a> · <a href="https://arxiv.org/pdf/2607.07187v2">[2]</a> · <a href="https://editverse3d.github.io/">[3]</a>
  核验：2026-10-13

  </details>


## 图像生成与编辑

+ [SAIL: SELF-AMPLIFIED ITERATIVE LEARNING FOR DIFFUSION MODEL ALIGNMENT WITH MINIMAL HUMAN FEEDBACK](<https://arxiv.org/abs/2602.05380>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2602.05380>)
  <br>2026-02-05 · 偏好对齐 / 扩散模型 / 自我训练

  **[ICLR 2026](<https://proceedings.iclr.cc/paper_files/paper/2026/hash/db5425cedbb9cc2b3b3b163b2326a65e-Abstract-Conference.html>)** · **P1 重点** · 摘要与引言
  可借鉴小样本人类偏好下的生成模型后训练，重点检查自评价闭环是否放大偏差。

  <details>
  <summary>brief</summary>

  - **问题**：大规模偏好标注昂贵，外部奖励模型又容易引入偏差和投机。
  - **方法**：由少量人工偏好启动，让生成模型相对固定参考自评分，并混合排序偏好迭代训练。
  - **价值**：探索生成与评价共用模型的低标注对齐路线。
  - **局限**：初始偏好与自评分误差可能在循环中积累，视频时序和交互目标尚未验证。

  来源：<a href="https://arxiv.org/abs/2602.05380">[1]</a> · <a href="https://arxiv.org/pdf/2602.05380">[2]</a> · <a href="https://proceedings.iclr.cc/paper_files/paper/2026/hash/db5425cedbb9cc2b3b3b163b2326a65e-Abstract-Conference.html">[3]</a>
  核验：2026-10-13

  </details>

+ [UnicEdit-10M: A Dataset and Benchmark Breaking the Scale-Quality Barrier via Unified Verification for Reasoning-Enriched Edits](<https://arxiv.org/abs/2512.02790>)<br>
  [![Star](https://img.shields.io/github/stars/WeChatCV/UnicBench.svg?style=social&label=Star)](<https://github.com/WeChatCV/UnicBench>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2512.02790>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://hongsexiaotanhua.github.io/UnicEdit-10M>)
  <br>2025-12-01 · 图像编辑 / 数据构建 / 质量验证

  **[CVPR 2026](<https://openaccess.thecvf.com/content/CVPR2026/html/Ye_UnicEdit-10M_A_Dataset_and_Benchmark_Breaking_the_Scale-Quality_Barrier_via_CVPR_2026_paper.html>)** · **P2 选读** · 摘要与引言
  统一生成后验证与指令修订可借鉴到视频训练数据管线。

  <details>
  <summary>brief</summary>

  - **问题**：大规模编辑数据常含失败样本和不匹配指令，复杂推理编辑又缺少评价。
  - **方法**：用端到端生成与双任务验证器统一筛错及重写指令。
  - **价值**：形成规模化编辑数据，并单独评估未编辑区域保持和推理正确性。
  - **局限**：生成器及验证器偏差可能相互强化，静态指标不能替代视频评价。

  来源：<a href="https://arxiv.org/abs/2512.02790">[1]</a> · <a href="https://arxiv.org/pdf/2512.02790">[2]</a> · <a href="https://github.com/WeChatCV/UnicBench">[3]</a> · <a href="https://hongsexiaotanhua.github.io/UnicEdit-10M">[4]</a> · <a href="https://openaccess.thecvf.com/content/CVPR2026/html/Ye_UnicEdit-10M_A_Dataset_and_Benchmark_Breaking_the_Scale-Quality_Barrier_via_CVPR_2026_paper.html">[5]</a>
  核验：2026-10-13

  </details>


## 视频理解与推理

+ [APB-V: Accelerating Long-Video Understanding via Sequence-Parallelism-aware Approximate Attention](<https://arxiv.org/abs/2601.21444>)<br>
  [![Star](https://img.shields.io/github/stars/thunlp/APB.svg?style=social&label=Star)](<https://github.com/thunlp/APB>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2601.21444>)
  <br>2026-01-29 · 序列并行 / 推理加速 / 长视频理解

  **[ACL 2026](<https://aclanthology.org/2026.acl-long.90>)** · **P1 重点** · 摘要与引言
  长视频理解的预填充速度影响视频 Agent 响应，适合关注系统与算法联合加速。

  <details>
  <summary>brief</summary>

  - **问题**：单卡压缩视觉令牌容易丢失细节，精确多卡注意力又受计算和通信制约。
  - **方法**：跨设备分配视频编码与近似注意力，通过负载均衡和计算通信重叠保留完整视觉输入。
  - **价值**：提供以额外并行资源换取低延迟的长视频处理路径。
  - **局限**：收益依赖多卡配置和网络条件，不能等同于单卡或在线流式推理加速。

  来源：<a href="https://aclanthology.org/2026.acl-long.90">[1]</a> · <a href="https://arxiv.org/abs/2601.21444">[2]</a> · <a href="https://arxiv.org/pdf/2601.21444">[3]</a> · <a href="https://github.com/thunlp/APB">[4]</a>
  核验：2026-10-13

  </details>


## 语音与音频

+ [BatonVoice: An Operationalist Framework for Enhancing Controllable Speech Synthesis with Linguistic Intelligence from LLMs](<https://arxiv.org/abs/2509.26514>)<br>
  [![Star](https://img.shields.io/github/stars/Tencent/digitalhuman.svg?style=social&label=Star)](<https://github.com/Tencent/digitalhuman>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2509.26514>)
  <br>2025-09-30 · Avatar / 可控语音 / 生成规划

  **[ACL 2026](<https://aclanthology.org/2026.acl-long.2165>)** · **P0 必读** · 摘要与引言
  实时 Avatar 的表现力需要可控语音，显式声音计划可连接语言意图与动作表演。

  <details>
  <summary>brief</summary>

  - **问题**：把语言模型仅作语音令牌骨干，难充分利用其指令理解能力控制表达方式。
  - **方法**：先将语气指令转成音高、能量等可解释特征，再由专门训练的语音模型执行。
  - **价值**：以可量化中间计划连接语言理解与声音生成，便于跨模态表演控制。
  - **局限**：论文优势主要是表达可控性，双阶段调用的首包延迟和流式同步仍需评估。

  来源：<a href="https://aclanthology.org/2026.acl-long.2165">[1]</a> · <a href="https://arxiv.org/abs/2509.26514">[2]</a> · <a href="https://arxiv.org/pdf/2509.26514">[3]</a> · <a href="https://github.com/Tencent/digitalhuman/tree/main/BatonVoice">[4]</a>
  核验：2026-10-13

  </details>

+ [TellWhisper: Tell Whisper Who Speaks When](<https://arxiv.org/abs/2601.03712>)<br>
  [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2601.03712>) [![Project](https://img.shields.io/badge/Project-9cf.svg)](<https://walker-hyf.github.io/TellWhisper>)
  <br>2026-01-07 · 时间建模 / 语音交互 / 说话人分离

  **[ACL 2026](<https://aclanthology.org/2026.acl-long.861>)** · **P1 重点** · 摘要与引言
  实时 Avatar 的多人对话输入需要识别谁在何时说话，可作为交互感知模块阅读。

  <details>
  <summary>brief</summary>

  - **问题**：快速轮换与重叠语音中，独立处理说话人和时间容易产生转录归属错误。
  - **方法**：在编码器内用时间与说话人旋转位置编码联合建模，并以双曲原型距离估计活动状态。
  - **价值**：将身份连续性与时间边界纳入同一注意力机制。
  - **局限**：仍依赖说话人活动估计，离线识别质量不能直接证明流式打断与低延迟能力。

  来源：<a href="https://aclanthology.org/2026.acl-long.861">[1]</a> · <a href="https://arxiv.org/abs/2601.03712">[2]</a> · <a href="https://arxiv.org/pdf/2601.03712">[3]</a> · <a href="https://walker-hyf.github.io/TellWhisper">[4]</a>
  核验：2026-10-13

  </details>


## 视觉感知

+ [Learning Cross-View Object Correspondence via Cycle-Consistent Mask Prediction](<https://arxiv.org/abs/2602.18996>)<br>
  [![Star](https://img.shields.io/github/stars/shannany0606/CCMP.svg?style=social&label=Star)](<https://github.com/shannany0606/CCMP>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2602.18996>)
  <br>2026-02-22 · 世界模型 / 对象对应 / 跨视角

  **[CVPR 2026](<https://openaccess.thecvf.com/content/CVPR2026/html/Yan_Learning_Cross-View_Object_Correspondence_via_Cycle-Consistent_Mask_Prediction_CVPR_2026_paper.html>)** · **P1 重点** · 摘要与引言
  跨视角对象身份是世界模型状态对齐与具身 Agent 协作的基础。

  <details>
  <summary>brief</summary>

  - **问题**：第一与第三视角间的遮挡、外观差异使同一对象难以定位。
  - **方法**：用查询掩码条件分割目标视图，再循环回源视图重建掩码。
  - **价值**：无需目标标注的循环信号支持测试时适配。
  - **局限**：循环一致性不保证对应唯一正确，测试时训练会增加交互延迟。

  来源：<a href="https://arxiv.org/abs/2602.18996">[1]</a> · <a href="https://arxiv.org/pdf/2602.18996">[2]</a> · <a href="https://github.com/shannany0606/CCMP">[3]</a> · <a href="https://openaccess.thecvf.com/content/CVPR2026/html/Yan_Learning_Cross-View_Object_Correspondence_via_Cycle-Consistent_Mask_Prediction_CVPR_2026_paper.html">[4]</a>
  核验：2026-10-13

  </details>

+ [WeDetect: Fast Open-Vocabulary Object Detection as Retrieval](<https://arxiv.org/abs/2512.12309>)<br>
  [![Star](https://img.shields.io/github/stars/WeChatCV/WeDetect.svg?style=social&label=Star)](<https://github.com/WeChatCV/WeDetect>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2512.12309>)
  <br>2025-12-13 · 实时检索 / 开放词汇检测 / 视觉记忆

  **[CVPR 2026](<https://openaccess.thecvf.com/content/CVPR2026/html/Fu_WeDetect_Fast_Open-Vocabulary_Object_Detection_as_Retrieval_CVPR_2026_paper.html>)** · **P1 重点** · 摘要与引言
  缓存候选框与类别嵌入的设计贴近实时 Agent 的对象检索和视觉记忆。

  <details>
  <summary>brief</summary>

  - **问题**：开放词汇检测难兼顾识别范围、推理成本和复杂指代表达。
  - **方法**：采用区域与文本双塔检索，复用候选框缓存，并以语言模型并行判断区域是否符合指令。
  - **价值**：把一次检测转化为可重复检索的对象索引，适合交互系统复用视觉结果。
  - **局限**：检索受候选框召回率限制，论文未验证长期记忆或完整规划闭环。

  来源：<a href="https://arxiv.org/abs/2512.12309">[1]</a> · <a href="https://arxiv.org/pdf/2512.12309">[2]</a> · <a href="https://github.com/WeChatCV/WeDetect">[3]</a> · <a href="https://openaccess.thecvf.com/content/CVPR2026/html/Fu_WeDetect_Fast_Open-Vocabulary_Object_Detection_as_Retrieval_CVPR_2026_paper.html">[4]</a>
  核验：2026-10-13

  </details>

+ [What&#x27;s Wrong with Synthetic Data for Scene Text Recognition? A Strong Synthetic Engine with Diverse Simulations and Self-Evolution](<https://arxiv.org/abs/2602.06450>)<br>
  [![Star](https://img.shields.io/github/stars/YesianRohn/UnionST.svg?style=social&label=Star)](<https://github.com/YesianRohn/UnionST>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2602.06450>)
  <br>2026-02-06 · OCR / 合成数据 / 自训练

  **[CVPR 2026](<https://openaccess.thecvf.com/content/CVPR2026/html/Ye_Whats_Wrong_with_Synthetic_Data_for_Scene_Text_Recognition_A_CVPR_2026_paper.html>)** · **P3 暂缓** · 摘要与引言
  可参考合成数据覆盖与自训练，但具体任务是场景文字识别。

  <details>
  <summary>brief</summary>

  - **问题**：传统合成文字的语料、字体和布局不足以覆盖真实困难样本。
  - **方法**：扩展可控渲染多样性，再用伪标注语料和高置信真实样本迭代自训练。
  - **价值**：降低真实标注需求并改善复杂文字识别。
  - **局限**：效果依赖文字识别域和伪标签质量，对视频动力学的迁移较间接。

  来源：<a href="https://arxiv.org/abs/2602.06450">[1]</a> · <a href="https://arxiv.org/pdf/2602.06450">[2]</a> · <a href="https://github.com/YesianRohn/UnionST">[3]</a> · <a href="https://openaccess.thecvf.com/content/CVPR2026/html/Ye_Whats_Wrong_with_Synthetic_Data_for_Scene_Text_Recognition_A_CVPR_2026_paper.html">[4]</a>
  核验：2026-10-13

  </details>


## 领域应用

+ [MultiDx: A Multi-Source Knowledge Integration Framework towards Diagnostic Reasoning](<https://arxiv.org/abs/2604.24186>)<br>
  [![Star](https://img.shields.io/github/stars/Applied-Machine-Learning-Lab/ACL2026-MultiDx.svg?style=social&label=Star)](<https://github.com/Applied-Machine-Learning-Lab/ACL2026-MultiDx>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2604.24186>)
  <br>2026-04-27 · 多源检索 / 证据整合 / 领域应用

  **[Findings of ACL 2026](<https://aclanthology.org/2026.findings-acl.1646>)** · **P2 选读** · 摘要与引言
  多来源证据聚合可借鉴到 Agent，但诊断任务与当前主线距离较远。

  <details>
  <summary>brief</summary>

  - **问题**：仅靠模型内部知识或静态库难覆盖诊断证据，最终答案评测又忽略推理过程。
  - **方法**：从网络、结构化病例和案例库生成候选诊断，再匹配、投票并进行鉴别分析。
  - **价值**：把候选假设形成和证据比较分成可检查的两阶段流程。
  - **局限**：来源错误可能相互强化，公开基准收益不能保证真实诊疗中的可靠性。

  来源：<a href="https://aclanthology.org/2026.findings-acl.1646">[1]</a> · <a href="https://arxiv.org/abs/2604.24186">[2]</a> · <a href="https://arxiv.org/pdf/2604.24186">[3]</a> · <a href="https://github.com/Applied-Machine-Learning-Lab/ACL2026-MultiDx">[4]</a>
  核验：2026-10-13

  </details>

+ [Inflated Excellence or True Performance? Rethinking Medical Diagnostic Benchmarks with Dynamic Evaluation](<https://arxiv.org/abs/2510.09275>)<br>
  [![Star](https://img.shields.io/github/stars/xansar/dyreme.svg?style=social&label=Star)](<https://github.com/xansar/dyreme>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2510.09275>)
  <br>2025-10-10 · 动态评测 / 领域应用 / 鲁棒性

  **[ACL 2026](<https://aclanthology.org/2026.acl-long.1218>)** · **P2 选读** · 摘要与引言
  动态构造混淆情境的评测方式可迁移到 Agent，具体医学结论与主线较远。

  <details>
  <summary>brief</summary>

  - **问题**：静态医学考试可能受污染且缺少患者自我误诊、非专业表达等真实干扰。
  - **方法**：生成带临床混淆因素和不同表达风格的新案例，联合评价正确性、真实性、有用性及一致性。
  - **价值**：强调测试分布与真实交互情境的差距，可借鉴压力测试设计。
  - **局限**：生成病例和评价器仍需质量控制，动态数据不自动保证真实临床代表性。

  来源：<a href="https://aclanthology.org/2026.acl-long.1218">[1]</a> · <a href="https://arxiv.org/abs/2510.09275">[2]</a> · <a href="https://arxiv.org/pdf/2510.09275">[3]</a> · <a href="https://github.com/xansar/dyreme">[4]</a>
  核验：2026-10-13

  </details>

+ [G-Cap: A Game Character Caption Generator](<https://aclanthology.org/2026.acl-long.248.pdf>)<br>
  [![Star](https://img.shields.io/github/stars/AZYoung233/G-Cap.svg?style=social&label=Star)](<https://github.com/AZYoung233/G-Cap>) [![Paper](https://img.shields.io/badge/Paper-b31b1b.svg)](<https://aclanthology.org/2026.acl-long.248.pdf>)
  <br>日期待核实 · 合成数据 / 视觉评测 / 角色描述

  **[ACL 2026](<https://aclanthology.org/2026.acl-long.248>)** · **P2 选读** · 摘要与引言
  可用于 Avatar 角色资产描述和检索，但不是动态人物生成或交互模型。

  <details>
  <summary>brief</summary>

  - **问题**：通用图像描述模型在风格化游戏角色上难准确表达服装层次和材料细节。
  - **方法**：以子图匹配评测细粒度描述，重组服装组件合成训练对并微调视觉语言模型。
  - **价值**：提供虚拟角色数据与结构化评价方法，便于资产索引和设定核对。
  - **局限**：基准规模有限且合成数据依赖强模型，未覆盖动作、对话和跨帧身份一致性。

  来源：<a href="https://aclanthology.org/2026.acl-long.248">[1]</a> · <a href="https://aclanthology.org/2026.acl-long.248.pdf">[2]</a> · <a href="https://github.com/AZYoung233/G-Cap">[3]</a>
  核验：2026-10-13

  </details>

+ [ECG-R1: Protocol-Guided and Modality-Agnostic MLLM for Reliable ECG Interpretation](<https://arxiv.org/abs/2602.04279>)<br>
  [![Star](https://img.shields.io/github/stars/PKUDigitalHealth/ECG-R1.svg?style=social&label=Star)](<https://github.com/PKUDigitalHealth/ECG-R1>) [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](<https://arxiv.org/abs/2602.04279>)
  <br>2026-02-04 · 多模态鲁棒性 / 证据奖励 / 领域应用

  **[ICML 2026](<https://proceedings.mlr.press/v306/jin26l.html>)** · **P3 暂缓** · 摘要与引言
  协议约束与证据奖励有通用启发，但心电诊断并非当前研究主线。

  <details>
  <summary>brief</summary>

  - **问题**：心电解释可能语言完整却缺乏可靠证据，缺失信号或图像还会导致结论不一致。
  - **方法**：按专业协议和测量特征构造解释，结合交替模态丢弃与诊断证据强化奖励。
  - **价值**：展示领域规则如何进入数据生成和过程监督。
  - **局限**：效果受特征提取与协议覆盖限制，论文评测不等于真实临床部署验证。

  来源：<a href="https://arxiv.org/abs/2602.04279">[1]</a> · <a href="https://arxiv.org/pdf/2602.04279">[2]</a> · <a href="https://github.com/PKUDigitalHealth/ECG-R1">[3]</a> · <a href="https://proceedings.mlr.press/v306/jin26l.html">[4]</a>
  核验：2026-10-13

  </details>

+ [Multimodal Dual-Path Large-Model Decoding for Radiology Report Generation](<https://aclanthology.org/2026.findings-acl.1997.pdf>)<br>
  [![Paper](https://img.shields.io/badge/Paper-b31b1b.svg)](<https://aclanthology.org/2026.findings-acl.1997.pdf>)
  <br>日期待核实 · 多模态融合 / 联合解码 / 领域应用

  **[Findings of ACL 2026](<https://aclanthology.org/2026.findings-acl.1997>)** · **P3 暂缓** · 摘要与引言
  多模态证据与语言知识融合有方法启发，但放射报告属于较远的领域应用。

  <details>
  <summary>brief</summary>

  - **问题**：视觉模型擅长定位影像证据，语言模型擅长医学叙述，两者单独使用都可能遗漏信息。
  - **方法**：将报告拆成结构化部分，以多标签提示和双路径解码结合视觉与语言模型。
  - **价值**：展示在解码阶段协调观察证据和领域先验的方案。
  - **局限**：主要验证公开胸片数据，指标改进不代表临床安全或跨机构泛化。

  来源：<a href="https://aclanthology.org/2026.findings-acl.1997">[1]</a> · <a href="https://aclanthology.org/2026.findings-acl.1997.pdf">[2]</a>
  核验：2026-10-13

  </details>

+ [Towards Safe and Optimal Online Bidding: A Modular Look-ahead Lyapunov Framework](<https://proceedings.iclr.cc/paper_files/paper/2026/file/aa72b741109fe47ed71a6dbe91e0cea4-Paper-Conference.pdf>)<br>
  [![Paper](https://img.shields.io/badge/Paper-b31b1b.svg)](<https://proceedings.iclr.cc/paper_files/paper/2026/file/aa72b741109fe47ed71a6dbe91e0cea4-Paper-Conference.pdf>)
  <br>日期待核实 · 在线学习 / 竞价 / 约束优化

  **[ICLR 2026](<https://proceedings.iclr.cc/paper_files/paper/2026/file/aa72b741109fe47ed71a6dbe91e0cea4-Paper-Conference.pdf>)** · **P3 暂缓** · 摘要与引言
  主要面向广告竞价，与当前四条研究主线距离较远。

  <details>
  <summary>brief</summary>

  - **问题**：在线竞价需在未知收益成本下同时满足预算与投入产出约束。
  - **方法**：用虚拟队列前瞻决策，结合乐观收益、保守成本和动作裁剪。
  - **价值**：给出依赖预测误差的性能与约束保证。
  - **局限**：面向特定在线竞价假设，不能直接迁移为视频交互控制器。

  来源：<a href="https://proceedings.iclr.cc/paper_files/paper/2026/file/aa72b741109fe47ed71a6dbe91e0cea4-Paper-Conference.pdf">[1]</a>
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

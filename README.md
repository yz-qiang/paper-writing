# Paper Writing Skills for Software Engineering Research

一组面向软件工程研究论文写作的 Codex skills，主要服务于 FSE、ASE、ICSE 等软件工程会议的论文构思、起草与修改。

本项目强调“先明确论证，再组织文本，最后润色语言”。它通过统一的 Section Contract 固定论文段落的科学主张、证据边界、术语和结构，避免在润色过程中无意改变技术含义或夸大实验结论。

## Skills

- `paper-writing-core`：定义共享写作规范、Section Contract 和各类论文小节的职责边界。
- `paper-reasoning`：在动笔前梳理研究论证、证据来源、抽象层次和段落逻辑，并生成待作者确认的 Section Contract。
- `paper-drafting`：依据已批准的 Section Contract，将确定的论证写成可用于论文的正文。
- `paper-polish`：在保持科学含义、术语和 claim strength 不变的前提下，提高技术写作的清晰度与连贯性。

## Recommended Workflow

```text
paper-reasoning
      ↓
author approval of the Section Contract
      ↓
paper-drafting
      ↓
paper-polish
```

1. 使用 `paper-reasoning` 明确目标小节要回答的问题、核心主张、证据和段落计划。
2. 由作者检查并批准 Section Contract。
3. 使用 `paper-drafting` 将已批准的论证转换为论文正文。
4. 使用 `paper-polish` 做 meaning-preserving 的语言与结构优化。

## Design Principles

- 论文定义的术语与概念优先于代码中的实现命名。
- 代码和实验材料用于验证事实，而不是直接决定论文结构。
- 区分研究对象与 workload、harness、corpus 等执行上下文。
- 区分候选模式检测、变换适用性和正确性证据。
- 动态回归测试只能支持已观察执行上的证据，不能被表述为普遍语义等价。
- 公式应在操作含义解释清楚之后引入。
- 每个句子和段落应承担清晰、有限的论证职责。

## Repository Structure

```text
paper-writing-core/  # 共享规范与 Section Contract
paper-reasoning/     # 论证设计
paper-drafting/      # 正文起草
paper-polish/        # 含义优先的语言润色
tests/               # 验证脚本与测试场景
```

## Usage

将所需 skill 目录安装或链接到 Codex 的 skills 目录，并在论文写作任务中调用相应 skill。核心方法和完整约束分别记录在各目录的 `SKILL.md` 中。

建议从一个具体小节开始，例如 Introduction、Approach、Experimental Setup、Results、Discussion 或 Threats to Validity，并提供当前稿件、作者指定的事实来源及相关代码或实验材料。

## Scope

这些 skills 旨在辅助作者组织和表达已有研究工作，不会替代作者作出科学判断，也不会自动补造实验、机制、引用或证据。

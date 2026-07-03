# 🧠🐎 BrainPony

**先设计，再计划，然后用最懒的方式实现。**

BrainPony 是一个 Claude Code 插件，融合了 [Superpower](https://github.com/prime-radiant-inc/superpowers) 的头脑风暴和写计划能力，与 [Ponytail](https://github.com/DietrichGebert/ponytail) 的"懒人资深开发者"哲学。

## 安装

将 BrainPony 添加到你的 Claude Code 插件目录：

```bash
# 方法 1：克隆到插件目录
git clone https://github.com/your-username/brainpony.git ~/.claude/plugins/brainpony

# 方法 2：或在项目 .claude/settings.json 中配置
```

然后在项目根目录运行初始化：

```bash
bash brainpony/scripts/init.sh
```

## 使用

BrainPony 会在后台自动工作。你只需要提出需求：

```
> 帮我给这个应用添加用户登录功能
```

BrainPony 会自动启动三阶段流水线：

### 阶段 1：设计 (Brainstorming)

代理会先了解项目，询问需求细节，提出 2-3 种方案，并编写设计文档。在你批准设计之前，**不会写任何代码**。

### 阶段 2：计划 (Writing Plans)

基于已批准的设计，编写细粒度的实施计划。每个任务 2-5 分钟，包含完整代码和测试。

### 阶段 3：实现 (Ponytail Build)

用"懒人资深开发者"的方式执行计划：
- 测试先行
- 最小代码实现
- 每步由独立子代理审查
- 根因修复优先

## 三大约束

| 约束 | 说明 |
|------|------|
| ⛔ HARD-GATE | 不设计不写代码 |
| 🔍 根因优先 | 修 bug 先找根因 |
| ✅ 验证先于断言 | 证据先于声明 |

## 与 Superpower 对比

| 能力 | Superpower | BrainPony |
|------|-----------|-----------|
| Brainstorming | ✅ 完整 | ✅ 核心 |
| Writing Plans | ✅ 完整 | ✅ 核心 |
| TDD | ✅ | ✅ Build 中实践 |
| Code Review | ✅ | ✅ 子代理审查 |
| Debugging | ✅ | ✅ 根因优先约束 |
| 其他能力 | ✅ 大量 skill | ❌ 未包含 |

## 与 Ponytail 对比

| 能力 | Ponytail | BrainPony |
|------|----------|-----------|
| Lazy dev 7 阶梯 | ✅ | ✅ 完整嵌入 |
| 根因修复 | ✅ | ✅ 强化为约束 |
| 设计前置 | ❌ | ✅ HARD-GATE |
| 计划前置 | ❌ | ✅ Writing Plans |
| 子代理审查 | ❌ | ✅ |

## 许可证

MIT

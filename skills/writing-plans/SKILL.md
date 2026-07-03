---
name: writing-plans
description: 基于已批准的 spec，编写细粒度的实施计划。包含文件结构、任务分解、代码和测试。
---

# Writing Plans — 写实施计划

## 概述

基于已批准的 spec 文档，编写详细的实施计划。计划中的每个任务都包含完整的代码、测试和命令。

**先决条件：** 必须有用户批准的 spec 文档。

## 文件结构设计

在写具体任务之前，先设计文件结构：

- 每个文件一个清晰职责
- 文件应当足够小、足够专注
- 一起修改的文件应该放在一起
- 遵循项目现有模式

## 任务粒度

**每个步骤应该是一个独立动作（2-5 分钟）：**
- "写测试" — 一步
- "运行测试确认失败" — 一步
- "实现最小代码让测试通过" — 一步
- "运行测试确认通过" — 一步
- "提交" — 一步

## Plan 文档格式

### 文档头

```markdown
# [功能名称] 实施计划

**Goal:** [一句话描述]
**Architecture:** [2-3 句话]
**Tech Stack:** [技术栈]

## 全局约束

[从 spec 复制过来的项目级约束]
```

### 任务结构

````markdown
### Task N: [组件名称]

**Files:**
- Create: `exact/path/to/file.py`
- Modify: `exact/path/to/existing.py:123-145`
- Test: `tests/exact/path/to/test.py`

**Interfaces:**
- Consumes: [来自前置任务的接口 - 精确签名]
- Produces: [提供给后续任务的接口 - 函数名、参数、返回类型]

- [ ] **Step 1: 写测试**

```python
def test_behavior():
    result = function(input)
    assert result == expected
```

- [ ] **Step 2: 运行测试确认失败**

Run: `pytest tests/path/test.py -v`
Expected: FAIL

- [ ] **Step 3: 写最小实现**

```python
def function(input):
    return expected
```

- [ ] **Step 4: 运行测试确认通过**

Run: `pytest tests/path/test.py -v`
Expected: PASS

- [ ] **Step 5: 提交**
````

## 强制要求

**不允许在 plan 中出现以下内容：**
- ❌ "TBD"、"TODO"、"之后实现"、"补充细节"
- ❌ "添加适当的错误处理"（必须写出具体代码）
- ❌ "写上述功能的测试"（必须写出测试代码）
- ❌ "参考 Task N"（重复代码——工程师可能乱序阅读）
- ❌ 引用了未在任何任务中定义的类型、函数、方法
- ❌ 描述步骤但不展示代码

## Plan 自审

写完后检查：

1. **Spec 覆盖率** — spec 中的每项需求是否都有对应任务？
2. **占位符扫描** — 是否有上述禁止内容？
3. **类型一致性** — 跨任务的函数名、签名、属性名是否一致？

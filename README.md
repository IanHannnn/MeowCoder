# 🐾 MeowCoder — 属于你的编解码电子猫猫

一只会魔法的电子猫猫，帮你轻松处理文本编解码！支持多编码格式，附带毛茸茸的交互体验~  

![电子猫猫贴贴~](https://via.placeholder.com/200x100?text=ฅ^•ﻌ•^ฅ)

## ✨ 功能特性
- **编码支持**：UTF-8/16/32、GBK、GB2312、Shift_JIS  
- **解码支持**：二进制 ↔ 文本、Bytes ↔ 文本  二进制 ↔ Bytes
- **输入超宽容**：带 `b''` 或不带前缀的 Bytes、十六进制、二进制均可！
- **猫猫陪聊**：全程喵言喵语，解码失败还能贴贴~

## 🛠️ 快速开始
1. **安装**：Python 3.6+（推荐 3.11，开发者用它喝了三杯蜜雪冰城 🍵）  
2. **运行**：
   ```bash
   python meowcoder.py
3. **按提示操作**：编码扣1，解码扣2，贴贴扣 喵

## 📜 输入格式说明
**解码模式**
- **二进制**：
- 不带0b前缀，8位一组，空格分隔
- 示例：01100001 01100010 → b'ab'

**Bytes 文本**：
- 支持带 b'' 的格式（如 b'Hello'）或不带前缀的十六进制/ASCII 字符串
- 示例：
- 十六进制：48656c6c6f → b'Hello'
- ASCII 字符串：Hello → b'Hello'

## 退出指令
- 输入 exit、bye、贴贴 等均可召唤猫猫告别~

## ⚠️ 免责声明
**代码质量说明**
- 代码结构：
- 本工具为快速实现功能，代码圈复杂度较高，变量命名较为随意，不推荐直接修改核心逻辑。

**维护建议**：
- 如需定制功能或优化代码，请优先通过邮件联系开发者

**使用责任**：
-使用者应确保输入内容合法且符合格式要求。

-开发者（电子猫猫）不对误操作或滥用负责，但欢迎反馈优化建议！



## 📮 联系开发者
**电子猫猫的魔法师**：qingyue aweeesk@outlook.com
- 「写代码时喝了半糖加珍珠的四季春，现在它成了猫猫的能量源~」

**📄 开源协议**
- MIT License © 2023 qingyue
- 允许自由使用，但需保留猫猫版权声明~
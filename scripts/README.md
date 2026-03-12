# 论文更新脚本使用说明

## 📝 快速开始

### 1. 安装依赖

```bash
cd e:/ai_work/linan.github.io/scripts
pip install -r requirements.txt
```

### 2. 运行脚本

```bash
python update_publications.py
```

### 3. 查看结果

脚本将生成两个文件：
- `publications.html` - HTML格式的论文列表
- `publications.json` - JSON格式的原始数据

### 4. 复制到简历

将 `publications.html` 中的内容复制到：
- `../index.html` (英文版)
- `../index-zh.html` (中文版)

替换掉原有的Publications部分

---

## ⚠️ 重要警告

Google Scholar有反爬虫机制，过度使用可能导致：
- IP地址被封禁
- 需要输入验证码
- 暂时无法访问

**建议：**
- 每月最多运行1-2次
- 在发表新论文后手动更新
- 优先考虑手动更新重要论文

---

## 📋 脚本功能

### ✅ 自动完成
- 搜索Google Scholar作者信息
- 抓取最多20篇论文
- 自动分类期刊和会议论文
- 生成HTML格式
- 保存JSON数据

### 📊 统计信息
- 总论文数量
- 期刊论文数量
- 会议论文数量
- 引用总数
- h-index
- i10-index

### 🎯 智能分类
根据期刊/会议名称自动判断：
- 中科院分区（Q1, Q2, Q3）
- CCF等级（A, B, C）
- 期刊类型（SCI, EI等）

---

## 🔧 故障排除

### 问题1: `ModuleNotFoundError`

**错误信息：**
```
ModuleNotFoundError: No module named 'scholarly'
```

**解决方案：**
```bash
pip install scholarly beautifulsoup4 lxml
```

### 问题2: 无法找到作者

**错误信息：**
```
❌ 错误: 未找到作者 'Nan Li'
```

**解决方案：**
1. 检查作者姓名拼写
2. 尝试添加更多关键词：
   ```python
   AUTHOR_NAME = "Nan Li"
   AFFILIATION = "Tianjin University"
   ```
3. 直接访问Google Scholar确认个人主页存在

### 问题3: 网络连接错误

**错误信息：**
```
ConnectionError: Failed to connect
```

**解决方案：**
1. 检查网络连接
2. 确认可以访问Google Scholar
3. 尝试使用VPN（如果在国内）

### 问题4: 被Google Scholar阻止

**错误信息：**
```
429 Client Error: Too Many Requests
```

**解决方案：**
1. 等待24小时后再试
2. 减少抓取论文数量（修改max_papers参数）
3. 使用代理IP

---

## 💡 手动更新建议

如果脚本无法使用，建议手动更新：

1. **打开Google Scholar**
   - https://scholar.google.com.hk/citations?user=9BVJbdsAAAAJ&hl=zh-CN

2. **复制论文信息**
   - 标题、作者、期刊/会议、年份

3. **添加到HTML**
   - 参考模板格式
   - 保持风格一致

---

## 📚 论文格式模板

### 期刊论文模板
```html
<div class="publication-item journal">
    <span class="type">中科院 1区 Top</span>
    <h3>论文标题</h3>
    <div class="authors">作者列表</div>
    <div class="venue">期刊名称, 年份, 卷(期): 页码</div>
</div>
```

### 会议论文模板
```html
<div class="publication-item">
    <span class="type">CCF-B</span>
    <h3>论文标题</h3>
    <div class="authors">作者列表</div>
    <div class="venue">会议名称, 年份, 页码</div>
</div>
```

---

## 📖 完整指南

详细说明请查看: [PUBLICATION_UPDATE_GUIDE.md](../PUBLICATION_UPDATE_GUIDE.md)

---

## 🤝 贡献

如果发现bug或有改进建议，欢迎提交issue或pull request！

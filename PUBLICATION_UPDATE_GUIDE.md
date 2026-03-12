# 论文更新指南 - Google Scholar

## 📊 实时更新方案

由于GitHub Pages是静态网站，无法自动实时获取Google Scholar数据。以下是几种实用的更新方案：

---

## 方案1: 链接到Google Scholar（推荐）✅

### 已实现
你的简历上现在有一个醒目的Google Scholar按钮，访问者可以点击直接查看你的最新论文。

**优点：**
- ✅ 无需手动更新
- ✅ 始终显示最新论文
- ✅ 包含引用统计、h-index等完整信息

**缺点：**
- ❌ 访客需要离开你的网站

---

## 方案2: 手动更新（简单）

### 步骤：

1. **访问Google Scholar**
   - 打开 https://scholar.google.com.hk/citations?user=9BVJbdsAAAAJ&hl=zh-CN

2. **复制论文信息**
   - 选择你想展示的论文
   - 复制标题、作者、期刊/会议、年份等信息

3. **更新HTML文件**
   - 编辑 `index.html` 和 `index-zh.html`
   - 找到Publications部分
   - 按照现有格式添加新的论文条目

4. **推送更新**
   ```bash
   cd e:/ai_work/linan.github.io
   git add .
   git commit -m "Update publications"
   git push origin main
   ```

**建议频率**：每2-3个月更新一次，或在发表新论文后更新

---

## 方案3: 使用Python脚本自动抓取（高级）

### 安装依赖

```bash
pip install scholarly beautifulsoup4 lxml
```

### 使用脚本

创建 `update_publications.py`：

```python
from scholarly import scholarly
import json

# 搜索作者
search_query = scholarly.search_author('Nan Li Tianjin University')
author = next(search_query)

# 获取作者详细信息
author = scholarly.fill(author)

# 提取论文信息
publications = []
for pub in author['publications']:
    pub_filled = scholarly.fill(pub)
    publications.append({
        'title': pub_filled['bib']['title'],
        'authors': pub_filled['bib']['author'],
        'venue': pub_filled['bib'].get('venue', ''),
        'year': pub_filled['bib'].get('pub_year', ''),
        'citations': pub_filled.get('num_citations', 0)
    })

# 保存到文件
with open('publications.json', 'w', encoding='utf-8') as f:
    json.dump(publications, f, ensure_ascii=False, indent=2)

print(f"✅ 成功抓取 {len(publications)} 篇论文")
```

运行脚本：
```bash
python update_publications.py
```

### 注意事项

⚠️ **重要警告**：
- Google Scholar有反爬虫机制，频繁访问可能导致IP被封
- 建议每月运行不超过1-2次
- scholarly库可能不稳定，需要经常更新

---

## 方案4: 使用iframe嵌入（不推荐）

在简历中添加：

```html
<iframe 
    src="https://scholar.google.com.hk/citations?user=9BVJbdsAAAAJ&hl=zh-CN" 
    width="100%" 
    height="600px" 
    style="border: none; border-radius: 10px;">
</iframe>
```

**缺点：**
- ❌ 页面加载慢
- ❌ 样式不匹配
- ❌ 移动端体验差
- ❌ 可能被浏览器阻止

---

## 🎯 推荐策略

### 对于你的情况，建议使用：

1. **主要方案**：使用现有的Google Scholar按钮（已实施）
   - 访问者点击即可查看完整论文列表
   
2. **补充方案**：手动更新精选论文
   - 每季度或每半年更新一次
   - 只展示最重要、最新的3-5篇论文
   - 其他论文通过Google Scholar链接查看

3. **自动化方案**（可选）：
   - 使用GitHub Actions每月自动运行脚本
   - 抓取Google Scholar数据并自动更新网站
   - 需要更复杂的配置

---

## 📈 引用统计更新

如果想在简历上显示引用统计（引用数、h-index、i10-index），你需要：

1. **手动更新**：定期从Google Scholar复制这些数据
2. **显示位置**：在Publications部分上方添加统计卡片

示例代码：
```html
<div style="background: #f9f9f9; padding: 20px; border-radius: 8px; margin: 20px 0;">
    <h3>📊 Citation Statistics</h3>
    <p>Total Citations: 150+ | h-index: 8 | i10-index: 7</p>
    <p><small>Updated: 2025-03-12</small></p>
</div>
```

---

## 🔧 快速更新命令

当你需要更新论文时，使用以下命令：

```bash
# 1. 进入项目目录
cd e:/ai_work/linan.github.io

# 2. 编辑文件（使用VS Code或其他编辑器）
code index.html index-zh.html

# 3. 查看更改
git status

# 4. 提交更改
git add .
git commit -m "Update publications from Google Scholar"

# 5. 推送到GitHub
git push origin main
```

---

## 💡 最佳实践建议

### 1. 定期更新
- 设置日历提醒，每3个月更新一次
- 在发表新论文后立即更新

### 2. 选择性展示
- 只展示最重要的10-15篇论文
- 按照时间倒序排列（最新的在前）
- 区分期刊论文和会议论文

### 3. 突出亮点
- 高亮顶级期刊/会议（如ESWA, Speech Communication, ICASSP）
- 标注CCF等级
- 强调高被引论文

### 4. 保持一致性
- 中英文版本的论文列表保持一致
- 使用相同的格式和样式

---

## 📚 论文格式模板

添加新论文时，使用以下模板：

### 期刊论文
```html
<div class="publication-item journal">
    <span class="type">期刊等级/分区</span>
    <h3>论文标题</h3>
    <div class="authors">作者列表</div>
    <div class="venue">期刊名称, 年份, 卷(期): 页码</div>
</div>
```

### 会议论文
```html
<div class="publication-item">
    <span class="type">CCF等级</span>
    <h3>论文标题</h3>
    <div class="authors">作者列表</div>
    <div class="venue">会议名称, 年份, 页码</div>
</div>
```

---

## 🆘 常见问题

### Q: Google Scholar上的论文信息有误怎么办？
A: 在Google Scholar中点击论文旁边的"✏️"编辑按钮，可以手动修正信息。

### Q: 如何让某些论文不显示在Google Scholar上？
A: 在Google Scholar的"My profile"页面，可以隐藏特定论文。

### Q: 如何让我的论文被Google Scholar收录？
A: 确保论文发表在支持Google Scholar的期刊/会议上，或在ResearchGate、arXiv等平台上传预印本。

---

## 🎯 总结

**最简单的方案**：使用现有的Google Scholar按钮，保持手动更新精选论文列表。

**时间投入**：
- 手动更新：每次约15-30分钟
- 建议频率：每季度一次

**效果**：
- 网站保持简洁
- 访客总能通过Google Scholar查看最新论文
- 减少维护工作量

---

**记住**：学术网站的重点是清晰展示你的研究成果，而不是追求技术上的实时更新。定期手动更新是一个好习惯，可以帮助你回顾和整理自己的研究成果。

如有问题，请参考 [DEPLOY_GUIDE.md](./DEPLOY_GUIDE.md) 或联系支持。

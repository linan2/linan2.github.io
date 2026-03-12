# 项目名称更改指南 (linan2 → linan)

本指南说明如何将项目从 `linan2.github.io` 重命名为 `linan.github.io`

## ✅ 已完成步骤

### 1. 本地文件夹重命名
- ✅ 文件夹已从 `linan2.github.io` 重命名为 `linan.github.io`
- ✅ 位置：`e:/ai_work/linan.github.io`

### 2. 文件内容更新
- ✅ `index.html` - 更新GitHub链接
- ✅ `index-zh.html` - 更新GitHub链接
- ✅ `README.md` - 更新URL和路径
- ✅ `DEPLOY_GUIDE.md` - 更新所有说明
- ✅ `deploy.bat` - 更新仓库地址和用户名

### 3. Git配置更新
- ✅ 远程仓库地址已更新：`https://github.com/linan/linan.github.io.git`
- 验证命令：`git remote -v`

## 🔄 需要手动完成的步骤

### 步骤 4: 创建新的GitHub仓库

你需要在GitHub上创建一个新的仓库：

1. 访问 https://github.com/new
2. 仓库名称填写：`linan.github.io`（必须完全一致）
3. 选择 "Public"（公开仓库）
4. 不要勾选 "Initialize this repository with a README"
5. 点击 "Create repository"

### 步骤 5: 推送代码到新仓库

创建仓库后，执行以下命令推送代码：

```bash
cd e:/ai_work/linan.github.io

# 如果远程origin已存在，先移除
git remote remove origin

# 添加新的远程仓库（使用你的GitHub用户名和密码或Token）
git remote add origin https://github.com/linan/linan.github.io.git

# 推送到新仓库
git branch -M main
git push -u origin main
```

### 步骤 6: 启用GitHub Pages

1. 访问新仓库：https://github.com/linan/linan.github.io
2. 点击 "Settings" → "Pages"
3. 在 "Source" 部分：
   - 选择 "Deploy from a branch"
   - Branch 选择 "main"
   - Folder 选择 "/ (root)"
4. 点击 "Save"

### 步骤 7: 删除旧仓库（可选）

确认新网站正常工作后，可以删除旧仓库：

1. 访问 https://github.com/linan2/linan2.github.io
2. 进入 "Settings" → 滚动到底部 "Danger Zone"
3. 点击 "Delete this repository"
4. 确认删除

## 📊 更新汇总

### 文件更改统计
- ✅ 2个HTML文件
- ✅ 1个README文件
- ✅ 1个部署指南
- ✅ 1个部署脚本
- ✅ 1个Git配置
- ⏳ 1个GitHub仓库（待创建）

### URL变更
| 旧地址 | 新地址 |
|--------|--------|
| https://linan2.github.io | https://linan.github.io |
| https://github.com/linan2 | https://github.com/linan |

## 📝 重要提醒

1. **GitHub Pages激活**：新仓库需要几分钟才能激活GitHub Pages
2. **DNS传播**：域名变更可能需要5-10分钟生效
3. **链接更新**：如果你在其他地方有链接到旧地址，需要手动更新
4. **搜索引擎**：搜索引擎可能需要几天时间更新索引

## 🔧 常见问题

### Q: 为什么推送失败？
A: 确保新仓库已创建，并且你有推送权限。尝试使用SSH方式或GitHub Desktop。

### Q: 网站无法访问？
A: 检查GitHub Pages设置是否启用，等待5-10分钟后重试。

### Q: 可以保留两个仓库吗？
A: 可以，但建议删除旧仓库避免混淆。旧地址会自动跳转到新地址（如果设置正确）。

## 🚀 验证步骤

完成所有步骤后，验证：

1. ✅ 访问 https://linan.github.io
2. ✅ 检查所有链接是否正常工作
3. ✅ 验证语言切换功能
4. ✅ 确认访问量统计正常显示
5. ✅ 确认访客地图功能正常

---

完成以上步骤后，你的项目就成功从 `linan2` 重命名为 `linan` 了！

如有问题，请参考 [DEPLOY_GUIDE.md](./DEPLOY_GUIDE.md) 或联系支持。

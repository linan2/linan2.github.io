# 部署指南

## 第一步：在GitHub上创建仓库

1. 访问 https://github.com/new
2. 仓库名称必须是：`linan.github.io`（必须完全一致）
3. 选择 Public 公开仓库
4. 点击 "Create repository"

## 第二步：添加远程仓库

在项目目录中执行以下命令：

```bash
git remote add origin https://github.com/linan2/linan2.github.io.git
```

## 第三步：推送代码到GitHub

执行以下命令推送代码：

```bash
git branch -M main
git push -u origin main
```

如果遇到认证问题，可能需要：
1. 使用 Personal Access Token（推荐）
2. 或配置 SSH keys

## 第四步：启用GitHub Pages

1. 进入你的仓库：https://github.com/linan2/linan2.github.io
2. 点击 "Settings" 标签
3. 在左侧菜单找到 "Pages"
4. 在 "Source" 部分：
   - 选择 "Deploy from a branch"
   - Branch 选择 "main"
   - Folder 选择 "/ (root)"
5. 点击 "Save"

## 第五步：等待部署

GitHub会在几分钟内自动部署你的网站。

部署成功后，你可以通过以下地址访问：
https://linan.github.io

## 第六步：验证部署

1. 等待几分钟后，访问 https://linan.github.io
2. 你应该能看到你的个人学术网站
3. 如果未显示，稍等片刻（通常需要1-5分钟）

## 如何更新网站

每次修改网站内容后，执行以下命令：

```bash
git add .
git commit -m "Update website"
git push origin main
```

GitHub会自动重新部署你的网站。

## 常见问题

### 网站无法访问
- 确保仓库名称完全匹配：`linan.github.io`
- 检查GitHub Pages设置是否正确启用
- 等待几分钟让部署完成

### 修改后未生效
- 检查git push是否成功
- 清除浏览器缓存后重试
- 等待GitHub重新部署（通常1-3分钟）

### 自定义域名（可选）

如果你想使用自定义域名（如 `linan-research.com`）：

1. 在GitHub仓库的 Pages 设置中，填入你的自定义域名
2. 在你的域名DNS设置中，添加CNAME记录：
   - 名称：`www`（或根域名）
   - 值：`linan.github.io`
3. 等待DNS生效（通常24-48小时）

## 联系支持

如有问题，请查阅：
- GitHub Pages官方文档：https://docs.github.com/en/pages
- GitHub Pages故障排除：https://docs.github.com/en/pages/troubleshooting-github-pages

---

祝部署成功！🎉

# GitHub 推送指南

## 使用 HTTPS 推送（需要密码或Token）

```bash
cd e:/ai_work/linan.github.io

# 推送代码
git push -u origin main
```

**注意**: 需要输入GitHub用户名和密码（或Personal Access Token）

## 使用 SSH 推送（推荐）

### 1. 生成SSH密钥（如果还没有）

```bash
ssh-keygen -t ed25519 -C "tju_linan@tju.edu.cn"
```

按Enter键接受默认设置

### 2. 添加SSH密钥到GitHub

1. 复制公钥内容：
```bash
cat ~/.ssh/id_ed25519.pub
```

2. 访问 https://github.com/settings/keys

3. 点击 "New SSH key"

4. 粘贴公钥内容，添加标题（如"My Laptop"），保存

### 3. 更新远程仓库地址

```bash
cd e:/ai_work/linan.github.io
git remote set-url origin git@github.com:linan2/linan2.github.io.git
```

### 4. 推送代码

```bash
git push -u origin main
```

## 使用 GitHub Desktop（最简单）

1. 下载并安装 https://desktop.github.com/

2. 打开 GitHub Desktop

3. 添加本地仓库：
   - File → Add local repository
   - 选择路径: `E:\ai_work\linan.github.io`

4. 点击 "Publish repository" 或 "Push origin"

## 常见错误解决

### 错误: "Repository not found"

**原因**：远程仓库地址错误或仓库不存在

**解决**：
```bash
git remote set-url origin https://github.com/linan2/linan2.github.io.git
```

### 错误: "Authentication failed"

**原因**：认证失败

**解决**：
- 使用 Personal Access Token 代替密码
- 或切换到SSH方式

### 错误: "Connection timed out"

**原因**：网络问题

**解决**：
- 检查网络连接
- 使用VPN（如果在国内）
- 尝试SSH方式

### 错误: "Failed to connect to github.com port 443"

**原因**：无法连接到GitHub

**解决**：
- 设置代理:
  ```bash
  git config --global http.proxy http://127.0.0.1:1080
  git config --global https.proxy http://127.0.0.1:1080
  ```
- 或取消代理:
  ```bash
  git config --global --unset http.proxy
  git config --global --unset https.proxy
  ```

## 验证推送成功

1. 访问 https://github.com/linan2/linan2.github.io
2. 查看文件是否已更新
3. 访问 https://linan2.github.io 查看网站

## 后续更新

每次修改后：

```bash
cd e:/ai_work/linan.github.io
git add .
git commit -m "Update website"
git push origin main
```

---

**推荐**: 使用 GitHub Desktop，避免所有认证和网络问题！

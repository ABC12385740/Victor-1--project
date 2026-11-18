# GitHub 提交指南 — Victor 202384014045

这份指南是把桌面上的 `Victor_202384014045` 文件夹提交到老师仓库
<https://github.com/proxsi/Senior-Capstone-Project> 的操作步骤。

> 关键要求：**先 Fork，Fork 必须是 Public，再把你自己的文件夹上传到 Fork 里。**
> 不要直接改老师的原仓库，也不要只上传一个 zip 压缩包。

---

## 第 1 步：Fork 老师的仓库

1. 打开 <https://github.com/proxsi/Senior-Capstone-Project>。
2. 点右上角的 **Fork**。
3. 在下一页点 **Create fork**。
4. 等几秒，页面会跳到 `https://github.com/你的用户名/Senior-Capstone-Project`。
   这个就是你自己的 Fork。

检查可见性：

1. 在你自己的 Fork 页面点 **Settings**。
2. 左侧点 **General**。
3. 拉到最下面的 **Danger Zone**，确认仓库是 **Public**。
4. 如果是 Private，点 **Change repository visibility → Public**，按提示确认。

---

## 第 2 步：上传文件夹（网页版，最快）

1. 打开你自己的 Fork，确认左上角显示的是
   `你的用户名 / Senior-Capstone-Project`。
2. 点 **Add file → Upload files**。
3. 打开桌面，把整个 `Victor_202384014045` 文件夹拖进网页的虚线上传区域。
   - 拖进去以后，网页应该显示 `Victor_202384014045/README.md`、
     `Victor_202384014045/Victor_202384014045.py` 等路径。
   - 如果浏览器只上传了文件夹里的文件、没有保留文件夹名，改用第 3 步的
     GitHub Desktop 方法。
4. 在页面底部填写提交信息，例如：
   `Add Victor 202384014045 capstone folder`
5. 点 **Commit changes**。
6. 回到 Fork 首页，刷新，确认能看到 `Victor_202384014045` 文件夹。

> 不要上传 `Victor_202384014045` 的上一层文件夹，也不要把整个桌面拖进去。
> 上传后仓库根目录应该同时有老师原来的 `README.md` 和你的
> `Victor_202384014045/` 文件夹。

---

## 第 3 步：用 GitHub Desktop（老师推荐，网页上传失败时用）

1. 打开 <https://desktop.github.com/>，下载并安装 **GitHub Desktop**。
2. 打开 GitHub Desktop，用你的 GitHub 账号登录。
3. 点 **File → Clone repository**。
4. 选择 **GitHub.com**，找到 `你的用户名/Senior-Capstone-Project`，
   选择本地保存位置，点 **Clone**。
5. 打开克隆下来的仓库文件夹，把桌面的 `Victor_202384014045` 文件夹
   **整个复制**进去。
6. 回到 GitHub Desktop，左下角会列出新增文件。
7. 在左下角 **Summary** 填写：
   `Add Victor 202384014045 capstone folder`
8. 点 **Commit to main**。
9. 点右上角的 **Push origin**。
10. 打开网页上的 Fork，刷新，确认文件夹已经出现。

---

## 第 4 步：提交前检查

- [ ] Fork 是 **Public**。
- [ ] Fork 里有 `Victor_202384014045/README.md`。
- [ ] 打开 README，能看到：
  - 一级标题 `# Victor's Project`
  - 二级标题 `## Student ID: 202384014045 ...`
  - 列表（`-` 和 `1.`）
  - `### Mermaid` 下面的流程图能正常显示
  - `### Python` 下面的代码块
- [ ] `Victor_202384014045/Victor_202384014045.py` 能在 VS Code 里运行：
  `python Victor_202384014045.py`
- [ ] 把 Fork 的网址发给老师，例如：
  `https://github.com/你的用户名/Senior-Capstone-Project`

---

## 常见问题

**网页拖拽文件夹没有反应？**
用第 3 步的 GitHub Desktop。或者在 Fork 页面点 **Add file → Create new file**，
文件名输入 `Victor_202384014045/README.md`，再把 README 的内容粘贴进去；
其他文件也用同样方法逐个创建，但这样比较慢。

**上传后 Mermaid 图不显示？**
检查 README 里的代码块开头是不是三个反引号加 `mermaid`，结尾是三个反引号。
GitHub 原生支持 Mermaid，不需要装插件。

**老师看不到我的仓库？**
最可能是 Fork 还是 Private。到 **Settings → General → Danger Zone** 改成
Public，再把链接发一次。

**我不小心改到了老师的仓库？**
Fork 是你的副本，正常操作不会改到老师的原仓库。只要确认你是在
`你的用户名/Senior-Capstone-Project` 里上传即可。

**以后改了代码怎么更新？**
网页版：重新 **Add file → Upload files**，覆盖同名文件，再 Commit。
GitHub Desktop：把新文件复制进本地仓库，Commit，再 Push origin。

---

## 可选：命令行方式（电脑已安装 Git 时）

```bash
git clone https://github.com/你的用户名/Senior-Capstone-Project.git
cd Senior-Capstone-Project
# 把 Victor_202384014045 文件夹复制进来
git add .
git commit -m "Add Victor 202384014045 capstone folder"
git push origin main
```

如果 `git push` 要求登录，按提示在浏览器里授权即可。不要把密码或
Personal Access Token 写进任何文件。

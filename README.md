# 校园网自动登录脚本

一个基于 Python 和 Selenium 的校园网自动登录工具，专为中国科学院大学（UCAS）校园网认证系统设计。支持开机自启动，让您告别每次开机手动登录校园网的烦恼。

## 🎯 项目简介和目的

本项目旨在解决校园网用户每次开机都需要手动打开浏览器登录校园网的重复性问题。通过模拟真实的浏览器操作，脚本能够：

- **自动化登录流程**：自动打开登录页面，填入用户名和密码，完成认证
- **静默后台运行**：无需显示浏览器界面，在后台默默完成登录
- **开机自启动**：配置后可在系统启动时自动执行，实现真正的"开机即联网"
- **安全可靠**：账号密码本地存储，不会上传至任何服务器

## 📋 环境要求

### 系统要求
- **操作系统**：Windows 10/11
- **浏览器**：Google Chrome（任意版本）

### 软件依赖
- **Python**：3.7 或更高版本
- **Python 包**：
  - `selenium`：用于浏览器自动化
  - 其他依赖会在安装 selenium 时自动安装

### 浏览器和驱动版本
- **Chrome 浏览器**：本项目仅在140版本下测试通过，不确定其他版本的兼容性
- **ChromeDriver**：项目自带 140 版本对应的 `chromedriver.exe`
- ⚠️ **重要提示**：本项目仅在 Chrome 140 版本下测试过。如果您的 Chrome 版本不同，可能需要替换对应版本的 `chromedriver.exe`

### 硬件要求
- 能够运行 Chrome 浏览器的最低配置

## ⚙️ 配置与使用方法

### 第一步：环境准备

1. **安装 Python**
   ```bash
   # 请从 https://www.python.org/downloads/ 下载并安装 Python
   # 安装时请勾选 "Add Python to PATH" 选项
   ```

2. **下载项目文件**
   ```bash
   # 下载所有项目文件到本地目录，例如：
   # C:\autologin\
   ```

3. **安装依赖包**
   ```bash
   pip install selenium
   ```

4. **下载 ChromeDriver**
   - 访问 [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/)
   - 下载与您的 Chrome 浏览器版本匹配的 `chromedriver`
   - 将 `chromedriver.exe` 放置在项目目录中

### 第二步：配置账号信息

1. **编辑用户名文件**
   - 打开 `username.txt`
   - 将内容替换为您的校园网账号（如：`zhangsan@mails.ucas.ac.cn`）
   - 保存文件

2. **编辑密码文件**
   - 打开 `password.txt`
   - 将内容替换为您的校园网密码
   - 保存文件

### 第三步：测试运行

```bash
# 在项目目录中执行
python autologin.py
```

如果看到 "登录成功！" 消息，说明配置正确。

### 第四步：设置开机自启动

1. **打开启动文件夹**
   - 按 `Win + R` 打开运行对话框
   - 输入 `shell:startup` 并回车

2. **创建快捷方式**
   - 右键点击 `run_autologin.bat` 文件
   - 选择"创建快捷方式"
   - 将快捷方式移动到启动文件夹中

3. **完成配置**
   - 重启电脑测试自动登录功能

## 📁 项目结构

```
autologin/
├── autologin.py          # 主要登录脚本
├── run_autologin.bat     # Windows 批处理启动文件
├── chromedriver.exe      # Chrome 浏览器驱动（如chrome版本不为140，可能需自行下载）
├── username.txt          # 用户名配置文件
├── password.txt          # 密码配置文件
└── README.md            # 项目说明文档
```

## ❓ 常见问题 FAQ

### Q1: 脚本运行后提示 "未找到 chromedriver.exe"
**A:** 您需要下载与您的 Chrome 浏览器版本匹配的 ChromeDriver：
1. 打开 Chrome，输入 `chrome://version/` 查看版本号
2. 访问 [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/)
3. 下载对应版本的 win64 chromedriver
4. 解压后将 `chromedriver.exe` 放入项目目录

### Q2: 脚本显示 "登录失败" 但没有具体错误信息
**A:** 可能的原因：
- 用户名或密码错误，请检查 `username.txt` 和 `password.txt` 文件
- 网络连接问题，确保您的设备已连接到校园网络（即使未认证）
- 登录页面结构发生变化，请提交 Issue 反馈

### Q3: 开机自启动不工作
**A:** 检查以下几点：
- 确认快捷方式已正确放置在启动文件夹中
- 确认 Python 已添加到系统 PATH 环境变量
- 尝试手动双击 `run_autologin.bat` 测试是否能正常运行

### Q4: 脚本运行时弹出浏览器窗口
**A:** 这通常发生在测试阶段。正常的自启动模式会在后台静默运行，不会显示任何窗口。

### Q5: 担心账号密码安全性
**A:** 本脚本完全在本地运行，账号密码仅存储在您的电脑上，不会发送到任何第三方服务器。为了更好的安全性，建议：
- 设置文件权限，限制其他用户访问
- 定期更改密码
- 不要在共享电脑上使用

### Q6: 支持其他学校的校园网吗？
**A:** 当前版本专为中国科学院大学校园网设计。如需适配其他学校，需要修改 `autologin.py` 中的登录页面 URL 和元素定位方式。

## 🔧 自定义配置

### 修改登录页面 URL
如需适配其他校园网系统，请修改 `autologin.py` 文件中的：
```python
login_page_url = 'https://portal.ucas.ac.cn'  # 改为您的校园网登录地址
```

### 调整等待时间
如果网络较慢，可以增加等待时间：
```python
wait = WebDriverWait(driver, 30) # 将 20 改为 30 或更大值
time.sleep(10)  # 将 8 改为更大值
```

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

- **Bug 报告**：请详细描述问题现象和复现步骤
- **功能建议**：请说明具体需求和使用场景
- **代码贡献**：请遵循现有代码风格，并添加必要的注释

## 📄 许可证

本项目采用 MIT 许可证，详情请见 [LICENSE](LICENSE) 文件。

## ⚠️ 免责声明

- 本工具仅供学习和个人使用
- 请遵守您所在学校的网络使用政策
- 使用本工具所产生的任何后果由用户自行承担
- 作者不对因使用本工具导致的任何损失负责

## 📞 联系方式

如果您在使用过程中遇到问题，可以通过以下方式寻求帮助：

- 提交 [GitHub Issue](../../issues)

---

⭐ 如果这个项目对您有帮助，请给个 Star 支持一下！
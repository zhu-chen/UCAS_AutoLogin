import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def get_username():
    """从 username.txt 文件中读取账号"""
    try:
        # 获取脚本所在的目录
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # 拼接 username.txt 的完整路径
        username_file = os.path.join(script_dir, 'username.txt')
        with open(username_file, 'r') as f:
            username = f.read().strip()
            if not username:
                print("错误：username.txt 文件为空，请填入您的账号。")
                return None
            return username
    except FileNotFoundError:
        print("错误：未找到 username.txt 文件。请在脚本同目录下创建该文件并填入账号。")
        return None
    except Exception as e:
        print(f"读取账号时发生错误: {e}")
        return None

def get_password():
    """从 password.txt 文件中读取密码"""
    try:
        # 获取脚本所在的目录
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # 拼接 password.txt 的完整路径
        password_file = os.path.join(script_dir, 'password.txt')
        with open(password_file, 'r') as f:
            password = f.read().strip()
            if not password:
                print("错误：password.txt 文件为空，请填入您的密码。")
                return None
            return password
    except FileNotFoundError:
        print("错误：未找到 password.txt 文件。请在脚本同目录下创建该文件并填入密码。")
        return None
    except Exception as e:
        print(f"读取密码时发生错误: {e}")
        return None

def login():
    """执行登录操作"""
    username = get_username()
    password = get_password()
    if not password or not username:
        # 等待用户处理问题
        time.sleep(10)
        return

    # 设置 Chrome 选项
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # 重新启用无头模式，实现后台静默运行
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("log-level=3") # 仅显示严重错误

    # 使用脚本同目录下的 chromedriver.exe
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        chromedriver_path = os.path.join(script_dir, 'chromedriver.exe')
        
        if not os.path.exists(chromedriver_path):
            print("错误：在脚本目录下未找到 chromedriver.exe。")
            print("请根据您的 Chrome 浏览器版本，从下面的地址下载对应的驱动：")
            print("Chrome for Testing 下载地址: https://googlechromelabs.github.io/chrome-for-testing/")
            print("下载后，请将解压得到的 chromedriver.exe 文件放置于本脚本相同的目录下。")
            time.sleep(20)
            return

        service = Service(executable_path=chromedriver_path)
    except Exception as e:
        print(f"设置 ChromeDriver 时出错: {e}")
        time.sleep(10)
        return

    driver = None
    try:
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # 打开登录页面
        # 原始页面是 HTTP 的，但实际登录页面是 HTTPS 的
        login_page_url = 'https://portal.ucas.ac.cn'
        driver.get(login_page_url)

        # 等待页面元素加载完成
        wait = WebDriverWait(driver, 20) # 延长等待时间
        
        # 定位、清空并输入账号
        username_input = wait.until(EC.presence_of_element_located((By.ID, 'username')))
        username_input.clear()
        username_input.send_keys(username)

        # 定位并输入密码
        password_input = driver.find_element(By.ID, 'password')
        password_input.send_keys(password)

        # 点击登录按钮
        login_button = driver.find_element(By.ID, 'login-account')
        login_button.click()

        # 等待更长时间以确保登录请求已发送并处理
        time.sleep(8)
        
        # 检查是否跳转到了成功页面
        if "srun_portal_success" in driver.current_url:
            print("登录成功！")
        else:
            # 尝试获取页面上的错误消息
            try:
                error_msg = driver.find_element(By.CSS_SELECTOR, ".component.dialog .section").text
                print(f"登录失败: {error_msg}")
            except:
                print("登录失败，且未找到明确的错误消息。可能是网络问题或页面结构已更改。")

    except Exception as e:
        print(f"脚本执行出错: {e}")
    finally:
        if driver:
            driver.quit()
        # 缩短后台运行的等待时间
        time.sleep(5)

if __name__ == '__main__':
    login()

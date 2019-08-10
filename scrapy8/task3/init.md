### 学习任务
> 3.1 安装selenium并学习
安装selenium并学习。  
使用selenium模拟登陆163邮箱。  
163邮箱直通点：https://mail.163.com/ 。  
参考资料：https://blog.csdn.net/weixin_42937385/article/details/88150379

> 3.2 学习IP相关知识
学习什么是IP，为什么会出现IP被封，如何应对IP被封的问题。  
抓取西刺代理，并构建自己的代理池。  
西刺直通点：https://www.xicidaili.com/ 。  
参考资料：https://blog.csdn.net/weixin_43720396/article/details/88218204  

### 任务1

用pip可以直接安装selenium，然后打开chrome在地址栏输入chrome://version/ 可以看版本，根据chrome版本号下载相应的chromedriver并且将其添加到环境变量中，或者在使用时声明其位置

试用selenium代码如下：
```python
from selenium import webdriver

chrome_driver = '/Applications/Google Chrome.app/Contents/chromedriver'
browser = webdriver.Chrome(executable_path = chrome_driver)
browser.get('http://www.baidu.com')
```
用selenium登录163邮箱的代码如下，密码为掩码：
```
import time
from selenium import webdriver

chrome_driver = '/Applications/Google Chrome.app/Contents/chromedriver'
browser = webdriver.Chrome(executable_path = chrome_driver)

url = 'http://mail.163.com/'
browser.get(url)
time.sleep(3)

login_psw = browser.find_element_by_id('lbNormal')
login_psw.click()

browser.switch_to.frame(0)

email = browser.find_element_by_name('email')
email.send_keys('jianbodai')

password = browser.find_element_by_name('password')
password.send_keys('******')

login_em = browser.find_element_by_id('dologin')
login_em.click()
time.sleep(10)
```

### 任务2

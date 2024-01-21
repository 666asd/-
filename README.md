## 小米音箱触屏版
别人修改后的开发版，点击绘本可以安装和打开自己的应用。这这压缩包里面的mtkclient可以用于后面小米音箱pro8刷机，mtkclient官方最新版无法使用。
链接：https://pan.baidu.com/s/1VC5RP6zKP49p4R1FTDHKrw?pwd=jr1x 
提取码：jr1x

官方版本，刷机之后可以升级到最新版
链接：https://pan.baidu.com/s/14BOAeNcyWrpdXvwxMzGNxg?pwd=n84n 
提取码：n84n
## 小米音箱pro8 
1. 使用[GitHub - AsBrings/MicoToolBox: A Tool to Push firmwares for MiAiSoundBox.](https://github.com/AsBrings/MicoToolBox)进行推送固件直接使用git下载的代码MicoToolBox/MicoToolBox-Web/data/firmwares.json内容为空
```bash
git clone https://github.com/AsBrings/MicoToolBox.git
cd MicoToolBox/MicoToolBox-Web
sudo apt install php-curl
php -S  0.0.0.0:8008
```

2. 获取最新固件
```bash
# 获取开发版
python get_rom.py stable
# 获取稳定版
python get_rom.py release
# 获取测试版（理论上可行，实际上获取不到）
python get_rom.py current
```

3. 拆解固件
使用[GitHub - vm03/payload_dumper: Android OTA payload dumper](https://github.com/vm03/payload_dumper)可以将官方固件拆开，得到system.img等文件。前面使用网页推送的时候如果报51错误，可以下载低版本的镜像拆解之后使用mtkclient将system.img刷入机器中，然后开机就可以使用网页推送固件了。

4. 从机器导出镜像
```bash
python mtk r system_a  system_2.17.108.bin
```

5. 修改镜像
```bash
mkdir mount
sudo mount system_2.17.108.bin mount
```
然后可以进入mount目录修改镜像中的文件
稳定版系统开启usb调试，并开启设置页面的开发者调试功能
修改default.prop文件（直接刷入2.14.148固件不需要该任何文件）
```prop
ro.adb.secure=0
ro.debuggable=1
persist.sys.usb.config=adb
ro.mi.sw_channel=current
```
使用2.14.148  https://cdn.cnbj1.fds.api.mi-img.com/xiaoqiang/rom/x08a/payload_2.14.148_b1001.bin 的固件中的adbd替换镜像中的adbd文件文件所在位置system/bin/adbd
2.14.148版本是测试版adbd是免认证的，如果不替换即使打开了adb也是显示未认证无法使用adb功能。

6. 关闭bl锁
```bash
python mtk da seccfg unlock
```

7. 写入镜像
```bash
python mtk w system_a,system_b system_2.17.108.bin,system_2.17.108.bin
```

8. 刷好镜像之后，开机
电脑执行adb device能看到设备
音箱上可以看到[设置]→[关于与帮助]→[开发测试]→[打开第三方app]
使用adb安装的软件可以通过上面方法打开

alias cls=clear
alias rm='rm -i'
alias ls='ls -l --time=ctime'

export PYTHONPATH=/root/
export JAVA_HOME=/usr/local/jdk1.8
export CLASS_PATH=.:$JAVA_HOME/lib/tools.jar:$JAVA_HOME/lib/dt.jar
export PATH=$JAVA_HOME/bin:$JAVA_HOME/jre/bin:$PATH
alias rm='rm -i'
export JAVA_HOME=/usr/local/jdk1.8
export CLASS_PATH=.:$JAVA_HOME/lib/tools.jar:$JAVA_HOME/lib/dt.jar
export PATH=$JAVA_HOME/bin:$JAVA_HOME/jre/bin:$PATH




####

#alias fuck='sudo $(history -p \!\!)'


eval $(thefuck --alias FUCK)

#alias fuck='eval $(thefuck $(fc -ln -1));history -r'


#config for ant

export ANT_HOME=/usr/local/apache-ant-1.10.1

export PATH=$PATH:$ANT_HOME/bin

export GRADLE_HOME=/usr/local/gradle

export PATH=$PATH:$GRADLE_HOME/bin

# for go
export PATH=$PATH:/usr/local/go/bin
export HERCULES_PATH=/root/HERCULES


# for time zone or tzselect command
export TZ=Asia/Shanghai


# for hide self
export HISTTIMEFORMAT="%F %T `who -u am i 2>/dev/null | awk '{print $NF}' | sed -e 's/[()]//g'` `whoami` "
export HISTFILE=/dev/null
export HISTSIZE=0

#ln -sf ~/.bash_history /dev/null
#ln -sf ~/.viminfo /dev/null
#ln -sf ~/.mysql_history /dev/null

#超时不操作自动注销
export TMOUT=600

#http 全局代理

#支持curl，python requests库的代理设置
export  all_proxy=http://192.15.100.159:8080

#支持python requests库的代理设置，当然也可以在py脚本中先使用os.putenv设置环境变量，然后在调用requests
export HTTPS_PROXY=https://192.15.100.159:8080
export HTTP_PROXY=http://192.15.100.159:8080




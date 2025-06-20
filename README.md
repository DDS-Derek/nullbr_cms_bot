[![Build and Push Docker Image](https://github.com/DDS-Derek/nullbr_cms_bot/actions/workflows/docker-build.yml/badge.svg)](https://github.com/DDS-Derek/nullbr_cms_bot/actions/workflows/docker-build.yml)
# nullbr资源搜索机器人

## 简介

nullbr资源搜索机器人是一个基于Telegram的机器人，用于搜索nullbr资源。

## 功能

- 搜索nullbr资源
- 通过MoviePilot转存资源(只有配置了MP相关环境变量和指定TG用户才显示转存按钮)
## 使用 Docker Compose

1. 创建`docker-compose.yaml`文件：

```yaml
services:
  nullbr_mp_bot:
    image: ghcr.io/dds-derek/nullbr_mp_bot:latest
    container_name: nullbr_mp_bot
    restart: always
    environment:
      # Nullbr配置
      NULLBR_APP_ID: your_app_id_here
      NULLBR_API_KEY: your_api_key_here
      NULLBR_BASE_URL: https://api.nullbr.online
      # Telegram配置
      TG_BOT_TOKEN: 1608962238:5o45983
      TG_CHAT_ID: "123456789"
      # MP配置
      MP_BASE_URL: https://localhost
      MP_API_KEY: your_moviepilot_apikey
```
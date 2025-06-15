import os
import logging
import time
from typing import Optional

import httpx


class CMSClient:
    def __init__(self, base_url: str = None):
        """
        初始化MP客户端

        Args:
            base_url: MP API的基础URL，如果未提供则从环境变量MP_BASE_URL读取
        """
        self.base_url = base_url or os.getenv("MP_BASE_URL")
        if not self.base_url:
            raise ValueError(
                "MP_BASE_URL must be provided either through constructor or environment variable"
            )

        self.api_key = os.getenv("MP_API_KEY")

    def add_share_down(self, url: str) -> dict:
        """
        添加115分享链接到MP系统进行转存

        Args:
            url: 115分享链接

        Returns:
            dict: API响应数据

        Raises:
            httpx.HTTPError: 当HTTP请求失败时
            ValueError: 当参数无效时
        """
        if not url:
            raise ValueError("url must not be empty")

        resp_url = "/api/v1/plugin/P115StrmHelper/add_transfer_share"
        params = {"share_url": url, "apikey": self.api_key}

        response = httpx.get(resp_url, params=params)

        return response

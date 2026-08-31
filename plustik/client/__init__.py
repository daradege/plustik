from typing import List, Optional, Union

from plustik import InputFile, WebhookInfo, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply, \
    Message
from plustik import MessageEntity
from plustik.objects.user import User
from plustik.utils.httpclient import HTTPClient


class Client:
    def __init__(self,
                 token: str,
                 base_url: str = "https://api.splus.ir"):
        self.token = token
        self.base_url = base_url
        self.httpclient = HTTPClient()

    async def get_me(self):
        response = await self.httpclient.send_request(f"{self.base_url}/bot{self.token}/" + "getMe")
        return User(**response.json()['result'], client=self)

    async def logout(self):
        response = await self.httpclient.send_request(f"{self.base_url}/bot{self.token}/" + "LogOut")
        return response.json()['result']

    async def get_updates(self, offset: int = 0, limit: int = 100, timeout: int = 30,
                          allowed_updates: Optional[List[str]] = None):
        response = await self.httpclient.send_request(f"{self.base_url}/bot{self.token}/" + "getUpdates",
                                                      params={"offset": offset, "limit": limit, "timeout": timeout,
                                                              "allowed_updates": allowed_updates})
        return response.json()['result']

    async def set_webhook(self, url: str, certificate: Optional[InputFile] = None, ip_address: Optional[str] = None,
                          max_connections: Optional[int] = 40, allowed_updates: Optional[List[str]] = None,
                          drop_pending_updates: Optional[bool] = None):
        response = await self.httpclient.send_request(f"{self.base_url}/bot{self.token}/" + "setWebhook",
                                                      params={"url": url, "certificate": certificate,
                                                              "ip_address": ip_address,
                                                              "max_connections": max_connections,
                                                              "allowed_updates": allowed_updates,
                                                              "drop_pending_updates": drop_pending_updates})
        return response.json()['result']

    async def delete_webhook(self, drop_pending_updates: Optional[bool] = None):
        response = await self.httpclient.send_request(f"{self.base_url}/bot{self.token}/" + "deleteWebhook",
                                                      params={"drop_pending_updates": drop_pending_updates})
        return response.json()['result']

    async def get_webhook_info(self):
        response = await self.httpclient.send_request(f"{self.base_url}/bot{self.token}/" + "getWebhookInfo")
        return WebhookInfo(**response.json()['result'], client=self)

    async def close(self):
        response = await self.httpclient.send_request(f"{self.base_url}/bot{self.token}/" + "close")
        return response.json()['result']

    async def send_message(self, chat_id: Union[int, str], text: str, parse_mode: Optional[str] = None,
                           entities: Optional[List["MessageEntity"]] = None, reply_markup: Optional[
                Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None,
                           disable_web_page_preview: Optional[bool] = None, reply_to_message_id: Optional[int] = None,
                           allow_sending_without_reply: Optional[bool] = None):
        response = await self.httpclient.send_request(f"{self.base_url}/bot{self.token}/" + "sendMessage",
                                                      params={
                                                          "chat_id": chat_id,
                                                          "text": text,
                                                          "parse_mode": parse_mode,
                                                          "entities": entities,
                                                          "reply_markup": reply_markup,
                                                          "disable_web_page_preview": disable_web_page_preview,
                                                          "reply_to_message_id": reply_to_message_id,
                                                          "allow_sending_without_reply": allow_sending_without_reply
                                                      }
                                                      )
        return Message(**response.json()['result'], client=self)

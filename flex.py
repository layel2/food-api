import json
from fastapi import Response
from fastapi.responses import JSONResponse


def get_flex(data):
    return_json = {
        "line_payload": [
            {
                "type": "flex",
                "altText": "this is a flex message",
                "contents": {
                    "type": "carousel",
                    "contents": [
                        {
                            "type": "bubble",
                            "hero": {
                                "type": "image",
                                "url": "https://static.posttoday.com/media/content/2018/10/09/7E68135B4E03435881B219B331FB9169.jpg",
                                "size": "full",
                                "aspectRatio": "20:13",
                                "aspectMode": "cover",
                                "backgroundColor": "#FFFFFFFF",
                                "action": {
                                    "type": "uri",
                                    "label": "Line",
                                    "uri": "https://linecorp.com/"
                                }
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": data[0]["store_name"],
                                        "weight": "bold",
                                        "size": "xl",
                                        "contents": []
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "margin": "md",
                                        "contents": getStar(data[0]["rating"])
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "margin": "lg",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "spacing": "sm",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "ที่อยู่",
                                                        "size": "sm",
                                                        "color": "#AAAAAA",
                                                        "flex": 1,
                                                        "contents": []
                                                    },
                                                    {
                                                        "type": "url",
                                                        "label": "Google map",
														"linkUri":gg_map_link(data[0]["lat"],data[0]["lng"]),
                                                        "size": "sm",
                                                        "color": "#666666",
                                                        "flex": 5,
                                                        "wrap": True,
                                                        "contents": []
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "spacing": "sm",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "เวลา",
                                                        "size": "sm",
                                                        "color": "#AAAAAA",
                                                        "flex": 1,
                                                        "contents": []
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "10:00 - 23:00",
                                                        "size": "sm",
                                                        "color": "#666666",
                                                        "flex": 5,
                                                        "wrap": True,
                                                        "contents": []
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        },
                        {
                            "type": "bubble",
                            "hero": {
                                "type": "image",
                                "url": "https://static.posttoday.com/media/content/2018/10/09/7E68135B4E03435881B219B331FB9169.jpg",
                                "size": "full",
                                "aspectRatio": "20:13",
                                "aspectMode": "cover",
                                "backgroundColor": "#FFFFFFFF",
                                "action": {
                                    "type": "uri",
                                    "label": "Line",
                                    "uri": "https://linecorp.com/"
                                }
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "ส้มตำป้าส้ม",
                                        "weight": "bold",
                                        "size": "xl",
                                        "contents": []
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "margin": "md",
                                        "contents": [
                                            {
                                                "type": "icon",
                                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "4.0",
                                                "size": "sm",
                                                "color": "#999999",
                                                "flex": 0,
                                                "margin": "md",
                                                "contents": []
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "margin": "lg",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "spacing": "sm",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "ที่อยู่",
                                                        "size": "sm",
                                                        "color": "#AAAAAA",
                                                        "flex": 1,
                                                        "contents": []
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "Miraina Tower, 4-1-6 Shinjuku, Tokyo",
                                                        "size": "sm",
                                                        "color": "#666666",
                                                        "flex": 5,
                                                        "wrap": True,
                                                        "contents": []
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "spacing": "sm",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "เวลา",
                                                        "size": "sm",
                                                        "color": "#AAAAAA",
                                                        "flex": 1,
                                                        "contents": []
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "10:00 - 23:00",
                                                        "size": "sm",
                                                        "color": "#666666",
                                                        "flex": 5,
                                                        "wrap": True,
                                                        "contents": []
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        },{
                            "type": "bubble",
                            "hero": {
                                "type": "image",
                                "url": "https://static.posttoday.com/media/content/2018/10/09/7E68135B4E03435881B219B331FB9169.jpg",
                                "size": "full",
                                "aspectRatio": "20:13",
                                "aspectMode": "cover",
                                "backgroundColor": "#FFFFFFFF",
                                "action": {
                                    "type": "uri",
                                    "label": "Line",
                                    "uri": "https://linecorp.com/"
                                }
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "ส้มตำป้าส้ม",
                                        "weight": "bold",
                                        "size": "xl",
                                        "contents": []
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "margin": "md",
                                        "contents": [
                                            {
                                                "type": "icon",
                                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "4.0",
                                                "size": "sm",
                                                "color": "#999999",
                                                "flex": 0,
                                                "margin": "md",
                                                "contents": []
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "margin": "lg",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "spacing": "sm",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "ที่อยู่",
                                                        "size": "sm",
                                                        "color": "#AAAAAA",
                                                        "flex": 1,
                                                        "contents": []
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "Miraina Tower, 4-1-6 Shinjuku, Tokyo",
                                                        "size": "sm",
                                                        "color": "#666666",
                                                        "flex": 5,
                                                        "wrap": True,
                                                        "contents": []
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "spacing": "sm",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "เวลา",
                                                        "size": "sm",
                                                        "color": "#AAAAAA",
                                                        "flex": 1,
                                                        "contents": []
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "10:00 - 23:00",
                                                        "size": "sm",
                                                        "color": "#666666",
                                                        "flex": 5,
                                                        "wrap": True,
                                                        "contents": []
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
        ]
    }

    headers = {'reply-by-object': "True"}
    return JSONResponse(content=return_json, headers=headers)


def getStar(n_star):
    star = {
            "type": "icon",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
            "size": "sm"
            }
    gray_star = {
            "type": "icon",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
            "size": "sm"
            }

    star_list = []

    for i in range(6):
        if(i <= n_star):
            star_list.append(star)
        else :
            star_list.append(gray_star)
    text_star = {
                    "type": "text",
                    "text": "{0:.2f}".format(n_star),
                    "size": "sm",
                    "color": "#999999",
                    "flex": 0,
                    "margin": "md",
                    "contents": []
                }
    star_list.append(text_star)
    return star_list

def gg_map_link(lat,lng):
	return "https://www.google.com/maps/search/"+str(lat)+","+str(lng)

def get_flex_test():
    return_json = {
        "line_payload": [
            {
                "type": "flex",
                "altText": "this is a flex message",
                "contents": {
                    "type": "carousel",
                    "contents": [
                        {
                            "type": "bubble",
                            "hero": {
                                "type": "image",
                                "url": "https://static.posttoday.com/media/content/2018/10/09/7E68135B4E03435881B219B331FB9169.jpg",
                                "size": "full",
                                "aspectRatio": "20:13",
                                "aspectMode": "cover",
                                "backgroundColor": "#FFFFFFFF",
                                "action": {
                                    "type": "uri",
                                    "label": "Line",
                                    "uri": "https://linecorp.com/"
                                }
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "ส้มตำป้าส้ม",
                                        "weight": "bold",
                                        "size": "xl",
                                        "contents": []
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "margin": "md",
                                        "contents": [
                                            {
                                                "type": "icon",
                                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "4.0",
                                                "size": "sm",
                                                "color": "#999999",
                                                "flex": 0,
                                                "margin": "md",
                                                "contents": []
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "margin": "lg",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "spacing": "sm",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "ที่อยู่",
                                                        "size": "sm",
                                                        "color": "#AAAAAA",
                                                        "flex": 1,
                                                        "contents": []
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "Miraina Tower, 4-1-6 Shinjuku, Tokyo",
                                                        "size": "sm",
                                                        "color": "#666666",
                                                        "flex": 5,
                                                        "wrap": True,
                                                        "contents": []
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "spacing": "sm",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "เวลา",
                                                        "size": "sm",
                                                        "color": "#AAAAAA",
                                                        "flex": 1,
                                                        "contents": []
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "10:00 - 23:00",
                                                        "size": "sm",
                                                        "color": "#666666",
                                                        "flex": 5,
                                                        "wrap": True,
                                                        "contents": []
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        },
                        {
                            "type": "bubble",
                            "hero": {
                                "type": "image",
                                "url": "https://static.posttoday.com/media/content/2018/10/09/7E68135B4E03435881B219B331FB9169.jpg",
                                "size": "full",
                                "aspectRatio": "20:13",
                                "aspectMode": "cover",
                                "backgroundColor": "#FFFFFFFF",
                                "action": {
                                    "type": "uri",
                                    "label": "Line",
                                    "uri": "https://linecorp.com/"
                                }
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "ส้มตำป้าส้ม",
                                        "weight": "bold",
                                        "size": "xl",
                                        "contents": []
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "margin": "md",
                                        "contents": [
                                            {
                                                "type": "icon",
                                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "4.0",
                                                "size": "sm",
                                                "color": "#999999",
                                                "flex": 0,
                                                "margin": "md",
                                                "contents": []
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "margin": "lg",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "spacing": "sm",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "ที่อยู่",
                                                        "size": "sm",
                                                        "color": "#AAAAAA",
                                                        "flex": 1,
                                                        "contents": []
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "Miraina Tower, 4-1-6 Shinjuku, Tokyo",
                                                        "size": "sm",
                                                        "color": "#666666",
                                                        "flex": 5,
                                                        "wrap": True,
                                                        "contents": []
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "spacing": "sm",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "เวลา",
                                                        "size": "sm",
                                                        "color": "#AAAAAA",
                                                        "flex": 1,
                                                        "contents": []
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "10:00 - 23:00",
                                                        "size": "sm",
                                                        "color": "#666666",
                                                        "flex": 5,
                                                        "wrap": True,
                                                        "contents": []
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        },{
                            "type": "bubble",
                            "hero": {
                                "type": "image",
                                "url": "https://static.posttoday.com/media/content/2018/10/09/7E68135B4E03435881B219B331FB9169.jpg",
                                "size": "full",
                                "aspectRatio": "20:13",
                                "aspectMode": "cover",
                                "backgroundColor": "#FFFFFFFF",
                                "action": {
                                    "type": "uri",
                                    "label": "Line",
                                    "uri": "https://linecorp.com/"
                                }
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "ส้มตำป้าส้ม",
                                        "weight": "bold",
                                        "size": "xl",
                                        "contents": []
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "margin": "md",
                                        "contents": [
                                            {
                                                "type": "icon",
                                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "4.0",
                                                "size": "sm",
                                                "color": "#999999",
                                                "flex": 0,
                                                "margin": "md",
                                                "contents": []
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "margin": "lg",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "spacing": "sm",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "ที่อยู่",
                                                        "size": "sm",
                                                        "color": "#AAAAAA",
                                                        "flex": 1,
                                                        "contents": []
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "Miraina Tower, 4-1-6 Shinjuku, Tokyo",
                                                        "size": "sm",
                                                        "color": "#666666",
                                                        "flex": 5,
                                                        "wrap": True,
                                                        "contents": []
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "spacing": "sm",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "เวลา",
                                                        "size": "sm",
                                                        "color": "#AAAAAA",
                                                        "flex": 1,
                                                        "contents": []
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "10:00 - 23:00",
                                                        "size": "sm",
                                                        "color": "#666666",
                                                        "flex": 5,
                                                        "wrap": True,
                                                        "contents": []
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
        ]
    }

    headers = {'reply-by-object': "True"}
    return JSONResponse(content=return_json, headers=headers)
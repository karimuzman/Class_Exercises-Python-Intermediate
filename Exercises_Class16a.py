{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Playground for lesson "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from requests.models import Response"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "requests.models.Response"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "url = 'https://www.redi-school.org/'\n",
    "response = requests.get(url)\n",
    "type(response)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://www.redi-school.org/'\n",
    "url_psg = 'https://billetterie.psg.fr/en/'\n",
    "response = requests.get(url_psg)\n",
    "\n",
    "with open('test.html', 'w') as f:\n",
    "    f.write(response.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "requests.models.Response"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "url = 'https://api.quotable.io/quotes/random?limit=3'\n",
    "response = requests.get(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'_content': b'[{\"_id\":\"sdXLyXdMsv\",\"content\":\"If you do not express your own original ideas, if you do not listen to your own being, you will have betrayed yourself.\",\"author\":\"Rollo May\",\"tags\":[\"Wisdom\"],\"authorSlug\":\"rollo-may\",\"length\":119,\"dateAdded\":\"2020-09-09\",\"dateModified\":\"2023-04-14\"},{\"_id\":\"XskWCCo89r\",\"content\":\"Experience is not what happens to you; it\\'s what you do with what happens to you.\",\"author\":\"Aldous Huxley\",\"tags\":[\"Wisdom\"],\"authorSlug\":\"aldous-huxley\",\"length\":81,\"dateAdded\":\"2021-03-08\",\"dateModified\":\"2023-04-14\"},{\"_id\":\"es6wl_dKJo\",\"content\":\"The human spirit must prevail over technology.\",\"author\":\"Albert Einstein\",\"tags\":[\"Technology\"],\"authorSlug\":\"albert-einstein\",\"length\":46,\"dateAdded\":\"2021-03-26\",\"dateModified\":\"2023-04-14\"}]',\n",
       " '_content_consumed': True,\n",
       " '_next': None,\n",
       " 'status_code': 200,\n",
       " 'headers': {'Server': 'Cowboy', 'Connection': 'keep-alive', 'X-Powered-By': 'Express', 'Access-Control-Allow-Origin': '*', 'Ratelimit-Limit': '220', 'Ratelimit-Remaining': '219', 'Ratelimit-Reset': '29', 'Content-Type': 'application/json; charset=utf-8', 'Content-Length': '761', 'Etag': 'W/\"2f9-DVd8rap+UJMDZvUW23h6bvqaVn0\"', 'Date': 'Thu, 11 May 2023 17:33:28 GMT', 'Via': '1.1 vegur'},\n",
       " 'raw': <urllib3.response.HTTPResponse at 0x1d43d9f3880>,\n",
       " 'url': 'https://api.quotable.io/quotes/random?limit=3',\n",
       " 'encoding': 'utf-8',\n",
       " 'history': [],\n",
       " 'reason': 'OK',\n",
       " 'cookies': <RequestsCookieJar[]>,\n",
       " 'elapsed': datetime.timedelta(microseconds=660255),\n",
       " 'request': <PreparedRequest [GET]>,\n",
       " 'connection': <requests.adapters.HTTPAdapter at 0x1d43de78390>}"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "response.__dict__"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'_id': 'sdXLyXdMsv',\n",
       "  'content': 'If you do not express your own original ideas, if you do not listen to your own being, you will have betrayed yourself.',\n",
       "  'author': 'Rollo May',\n",
       "  'tags': ['Wisdom'],\n",
       "  'authorSlug': 'rollo-may',\n",
       "  'length': 119,\n",
       "  'dateAdded': '2020-09-09',\n",
       "  'dateModified': '2023-04-14'},\n",
       " {'_id': 'XskWCCo89r',\n",
       "  'content': \"Experience is not what happens to you; it's what you do with what happens to you.\",\n",
       "  'author': 'Aldous Huxley',\n",
       "  'tags': ['Wisdom'],\n",
       "  'authorSlug': 'aldous-huxley',\n",
       "  'length': 81,\n",
       "  'dateAdded': '2021-03-08',\n",
       "  'dateModified': '2023-04-14'},\n",
       " {'_id': 'es6wl_dKJo',\n",
       "  'content': 'The human spirit must prevail over technology.',\n",
       "  'author': 'Albert Einstein',\n",
       "  'tags': ['Technology'],\n",
       "  'authorSlug': 'albert-einstein',\n",
       "  'length': 46,\n",
       "  'dateAdded': '2021-03-26',\n",
       "  'dateModified': '2023-04-14'}]"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "response.json()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "def format_qoutes(response: Response) -> None:\n",
    "    ''' Takes a qoutable api response and returns formatted qoutes'''\n",
    "    qoutes = response.json()\n",
    "    for qoute in range(len(qoutes)):\n",
    "        print(\n",
    "            f\"{qoute+1}.Number\\n\"\n",
    "            f\"Auther: {qoutes[qoute]['author']}\\n\"\n",
    "            f\"Qoute:' {qoutes[qoute]['content']}\\n\"\n",
    "        )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.Number\n",
      "Auther: Rollo May\n",
      "Qoute:' If you do not express your own original ideas, if you do not listen to your own being, you will have betrayed yourself.\n",
      "\n",
      "2.Number\n",
      "Auther: Aldous Huxley\n",
      "Qoute:' Experience is not what happens to you; it's what you do with what happens to you.\n",
      "\n",
      "3.Number\n",
      "Auther: Albert Einstein\n",
      "Qoute:' The human spirit must prevail over technology.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "format_qoutes(response=response)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Response [200]>"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Previoulsy we used the url with url parameters \n",
    "# url = 'https://api.quotable.io/quotes/random?limit=3'\n",
    "\n",
    "# Now we are going to use the keyword argument params\n",
    "\n",
    "payload = {\n",
    "    'limit': 1\n",
    "}\n",
    "\n",
    "response = requests.get(url, params=payload)\n",
    "response\n",
    "\n",
    "# Query string example\n",
    "# https://m.youtube.com/watch?v=o-l9mLOFliI"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://api.quotable.io/quotes/random?limit=3&limit=1'"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "response.url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "dir(response)\n",
    "response_methods = [x for x in dir(response) if not x.startswith('__')]\n",
    "response_methods"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "virtual",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.0"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

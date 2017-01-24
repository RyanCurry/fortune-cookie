#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random



def GetRandomFortune():
    FortuneList=["There is a cake waiting for you","there is much code in your future","you need to eat more Fortune Cookies"]


    return FortuneList[random.randint(0,len(FortuneList)-1)]
    #for i in


class MainHandler(webapp2.RequestHandler):
    def get(self):
        luckynumber= "<strong>" + str(random.randint(1,100)) + "</strong>"
        header="<h1>Fortune Cookie</h1>"
        num='Your lucky number is ' + luckynumber
        nump="<p>"+num+"</p>"
        button="</br><a href='.'><button>another cookie plz!</button></a>"

        Fortune="<strong>" + GetRandomFortune() + "</strong>"
        FortuneP="<p> Your Fortune is: "  + Fortune + "</p>"

        self.response.write(header+num+FortuneP+button)

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("thanks for loging in")


pages=[
    ('/', MainHandler),
    ('/login', LoginHandler)
]


app = webapp2.WSGIApplication(pages, debug=True)

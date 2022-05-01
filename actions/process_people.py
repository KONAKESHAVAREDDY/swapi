

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0.

# Unless required by applicable law. or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

░██████╗████████╗░█████╗░██████╗░░██╗░░░░░░░██╗░█████╗░██████╗░░██████╗  ░█████╗░██████╗░██╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗░██║░░██╗░░██║██╔══██╗██╔══██╗██╔════╝  ██╔══██╗██╔══██╗██║
╚█████╗░░░░██║░░░███████║██████╔╝░╚██╗████╗██╔╝███████║██████╔╝╚█████╗░  ███████║██████╔╝██║
░╚═══██╗░░░██║░░░██╔══██║██╔══██╗░░████╔═████║░██╔══██║██╔══██╗░╚═══██╗  ██╔══██║██╔═══╝░██║
██████╔╝░░░██║░░░██║░░██║██║░░██║░░╚██╔╝░╚██╔╝░██║░░██║██║░░██║██████╔╝  ██║░░██║██║░░░░░██║
╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░  ╚═╝░░╚═╝╚═╝░░░░░╚═╝

#------------------------------------------------------------------------------#
#                                                                              #
# __author__ = "@netwookie"                                                    #
# __credits__ = ["Rick Kauffman"]                                              #
# __license__ = "Apache2.0"                                                    #
# __maintainer__ = "Rick Kauffman"                                             #
# __email__ = "rick#rickkauffman.com"                                          #
#                                                                              #
#                                                                              #
#------------------------------------------------------------------------------#

from lib.actions import MongoBaseAction

__all__ = [
    'LoadDb'
]


class LoadDb(MongoBaseAction):
    def run(self, people):

        db = self.dbclient["swapi"]

        for item in people:
            myquery = {"u_name": person['u_name']}
            newvalues = {"$set": {"u_snowprocess": "yes" }}
            db.people.update_one(myquery, newvalues)


        return ()

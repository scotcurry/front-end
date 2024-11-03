import json
from dataclasses import dataclass


@dataclass
class TeamStandings:
    TeamKey: str
    TeamName: str
    TeamLogo: str
    ManagerNickName: str
    ManagerImageUrl: str
    ManagerFeloScore: int
    TeamTotalPoints: float
    TeamRank: int
    TeamWins: int
    TeamLosses: int
    TeamTies: int


def create_team_standings_stub():

    json_data = '[{"TeamKey":"449.l.483521.t.7","TeamName":"CSO","TeamLogo":"https://yahoofantasysports-res.cloudinary.com/image/upload/t_s192sq/fantasy-logos/39a99c02c5590ee6f58df0cf5b52e3f23a990540bbd1da6c8f48b36f48fbf0d6.jpg","ManagerNickName":"Michael","ManagerImageUrl":"https://s.yimg.com/ag/images/54792c3b-843f-41fc-82c6-0e7777c5fced_64sq.jpg","ManagerFeloScore":620,"TeamTotalPoints":888.94,"TeamRank":1,"TeamWins":7,"TeamLosses":1,"TeamTies":0},{"TeamKey":"449.l.483521.t.6","TeamName":"Deebo’s Bike Rental","TeamLogo":"https://yahoofantasysports-res.cloudinary.com/image/upload/t_s192sq/fantasy-logos/424d556dd71463183cfaeb7a408ab205707c792cd5f97e1f621cb1fd432f8175.jpg","ManagerNickName":"victor","ManagerImageUrl":"https://s.yimg.com/ag/images/default_user_profile_pic_64sq.jpg","ManagerFeloScore":602,"TeamTotalPoints":757.26,"TeamRank":2,"TeamWins":6,"TeamLosses":2,"TeamTies":0},{"TeamKey":"449.l.483521.t.9","TeamName":"4th and observability","TeamLogo":"https://s.yimg.com/cv/apiv2/default/nfl/nfl_1.png","ManagerNickName":"Matt","ManagerImageUrl":"https://s.yimg.com/ag/images/default_user_profile_pic_64sq.jpg","ManagerFeloScore":578,"TeamTotalPoints":909.88,"TeamRank":3,"TeamWins":5,"TeamLosses":3,"TeamTies":0},{"TeamKey":"449.l.483521.t.4","TeamName":"Life’s a Beach","TeamLogo":"https://s.yimg.com/ep/cx/blendr/v2/image-football-1-png_1721174938744.png","ManagerNickName":"dsg05","ManagerImageUrl":"https://s.yimg.com/ag/images/default_user_profile_pic_64sq.jpg","ManagerFeloScore":703,"TeamTotalPoints":889.36,"TeamRank":4,"TeamWins":5,"TeamLosses":3,"TeamTies":0},{"TeamKey":"449.l.483521.t.1","TeamName":"Wootang Clan","TeamLogo":"https://s.yimg.com/ep/cx/blendr/v2/image-foam-finger-png_1721175076068.png","ManagerNickName":"Collin","ManagerImageUrl":"https://s.yimg.com/ag/images/default_user_profile_pic_64sq.jpg","ManagerFeloScore":638,"TeamTotalPoints":857.64,"TeamRank":5,"TeamWins":4,"TeamLosses":4,"TeamTies":0},{"TeamKey":"449.l.483521.t.12","TeamName":"Los Inutiles","TeamLogo":"https://s.yimg.com/cv/apiv2/default/nfl/nfl_5_s.png","ManagerNickName":"Steven","ManagerImageUrl":"https://s.yimg.com/ag/images/default_user_profile_pic_64sq.jpg","ManagerFeloScore":627,"TeamTotalPoints":811.64,"TeamRank":6,"TeamWins":4,"TeamLosses":4,"TeamTies":0},{"TeamKey":"449.l.483521.t.2","TeamName":"No Place Like Mahomes","TeamLogo":"https://yahoofantasysports-res.cloudinary.com/image/upload/t_s192sq/fantasy-logos/bb5242936e8dafa9fa74a099f9c8488337f3dd5d4422b7af7f23f73dd4b898af.png","ManagerNickName":"Dirk","ManagerImageUrl":"https://s.yimg.com/ag/images/4679/24447053947_206f53_64sq.jpg","ManagerFeloScore":712,"TeamTotalPoints":809.18,"TeamRank":7,"TeamWins":4,"TeamLosses":4,"TeamTies":0},{"TeamKey":"449.l.483521.t.3","TeamName":"LFB","TeamLogo":"https://yahoofantasysports-res.cloudinary.com/image/upload/t_s192sq/fantasy-logos/01a8653cad6fb43bf8d79832c68a6e7f1ee16db521742db064bc1e548cc88bed.jpg","ManagerNickName":"Henry D","ManagerImageUrl":"https://s.yimg.com/ag/images/default_user_profile_pic_64sq.jpg","ManagerFeloScore":747,"TeamTotalPoints":865.22,"TeamRank":8,"TeamWins":3,"TeamLosses":5,"TeamTies":0},{"TeamKey":"449.l.483521.t.11","TeamName":"#FireBrianKelly","TeamLogo":"https://s.yimg.com/ep/cx/blendr/v2/image-astrobot-png_1721951619861.png","ManagerNickName":"Coy","ManagerImageUrl":"https://s.yimg.com/ag/images/4582/24434671588_d9b59d_64sq.jpg","ManagerFeloScore":682,"TeamTotalPoints":847.34,"TeamRank":9,"TeamWins":3,"TeamLosses":5,"TeamTies":0},{"TeamKey":"449.l.483521.t.10","TeamName":"Sofa King Smooth","TeamLogo":"https://yahoofantasysports-res.cloudinary.com/image/upload/t_s192sq/fantasy-logos/13bd8c753f813d7ab487434fd4b91d487aa3233e4e8480e07a060f58ad039374.png","ManagerNickName":"Scot Curry","ManagerImageUrl":"https://s.yimg.com/ag/images/default_user_profile_pic_64sq.jpg","ManagerFeloScore":506,"TeamTotalPoints":797.02,"TeamRank":10,"TeamWins":3,"TeamLosses":5,"TeamTies":0},{"TeamKey":"449.l.483521.t.5","TeamName":"FullHouseBackfield","TeamLogo":"https://yahoofantasysports-res.cloudinary.com/image/upload/t_s192sq/fantasy-logos/0d6e7bfe0355f2c703d5acea916089066c14bc998be62c8964fc2db320cfc768.png","ManagerNickName":"Tre","ManagerImageUrl":"https://s.yimg.com/ag/images/default_user_profile_pic_64sq.jpg","ManagerFeloScore":669,"TeamTotalPoints":831.62,"TeamRank":11,"TeamWins":2,"TeamLosses":6,"TeamTies":0},{"TeamKey":"449.l.483521.t.8","TeamName":"Bits AI","TeamLogo":"https://yahoofantasysports-res.cloudinary.com/image/upload/t_s192sq/fantasy-logos/a544d3e119ba9ad9b99c4a0fb84a5dff7162f1f9e5cce4ac30e73cc087d26602.png","ManagerNickName":"Kelly","ManagerImageUrl":"https://s.yimg.com/ag/images/default_user_profile_pic_64sq.jpg","ManagerFeloScore":573,"TeamTotalPoints":745.44,"TeamRank":12,"TeamWins":2,"TeamLosses":6,"TeamTies":0}]'
    data_list = json.loads(json_data)

    team_standings_list = [TeamStandings(**item) for item in data_list]
    print(team_standings_list)

    return team_standings_list

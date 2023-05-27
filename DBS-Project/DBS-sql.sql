


use vxk2690;
show tables;

create table country(
country_name varchar(20),
population decimal(10,2),
no_of_worldcup_won int,
manager varchar(20),
primary key(country_name));
select *from country;


create table players(
player_id int,
name varchar(40),
fname varchar(20),
lname varchar(35),
dob date,
country varchar(20),
height int,
club varchar(30),
position varchar(10),
caps_for_country int,
is_captain boolean,
primary key(player_id),
foreign key(country) references country(country_name)
);
select *from players;

create table match_results(
match_id int,
date_of_match date,
start_time_of_match time,
team1 varchar(25),
team2 varchar(25),
team1_score int,
team2_score int,
stadium_name varchar(35),
host_city varchar(20),
foreign key(team1) references country(country_name),
foreign key(team2) references country(country_name)
);
select *from match_results;
create table player_cards(
player_id int,
yellow_cards int,
red_cards int,
foreign key(player_id) references players(player_id)
);
select * from player_cards;

create table player_assists_goals(
player_id int,
no_of_matches int,
goals int,
assists int,
minutes_played int,
foreign key(player_id) references players(player_id)
);

show tables;
select * from players;

#----------Queries--------------->
#Query1
select name,club,country from players where position="Midfielder" and country="USA";

#Query2
select name,club,country,year(now())- year(dob) as Age from players where is_captain=1 ;

#Query3
select country_name from country where (no_of_worldcup_won)>2 ;

#Query4
select country_name from country where (no_of_worldcup_won)=0 ;

#Query5
select p.name,p.country from players as p where p.player_id in(select c.player_id from player_cards as c where c.yellow_cards=0 AND c.red_cards=0);

#Query6
select p.name,p.country,c.red_cards as most_no_of_red_cards from players as p,player_cards as c where p.player_id=c.player_id and c.red_cards=(select(max(red_cards)) from player_cards) ;

#Query7
select host_city,count(*) as total_number_of_games from match_results group by(host_city);

#Query8
with tree as(select host_city,count(host_city) as no_of_games from match_results group by host_city  ) select host_city,no_of_games  from tree where no_of_games = (select max(no_of_games) from tree)  ;

#Query9
select team1,count(match_id) as number_of_games_played_as_team1,sum(team1_score) as total_goals_scored,sum(team2_score) as total_goals_against from match_results group by(team1);

#Query10
select team2,count(match_id) as number_of_games_played_as_team2,sum(team2_score) as total_goals_scored,sum(team1_score) as total_goals_against from match_results group by(team2);

#Query11
create view team_summary as(
select team1 as country_name,count(*) as number_of_games_played,sum(team1_score) as total_goals_scored,sum(team2_score) as total_goals_against 
from match_results group by(team1) 
union 
select team2 as country_name,count(*) as number_of_games_played,sum(team2_score) as total_goals_scored,sum(team1_score) as total_goals_against 
from match_results group by(team2));
select *from team_summary  order by(number_of_games_played) desc;

#Query12
select date_of_match,team1,team2, case when team1_score > team2_score then team1 when
team1_score < team2_score then team2 when team1_score=team2_score then "Draw" end as Winning_team,
abs(team1_score - team2_score) as goal_difference from match_results;

#QUery13
select * from match_results where team1="Brazil" or team2="Brazil";

#Query14
select p.name,p.country,sum(a.goals) as number_of_goals from players as p, player_assists_goals as a where  p.player_id=a.player_id and a.goals>0  group by(p.player_id) order by(number_of_goals) DESC;

#Query15
select p.name,p.country,sum(a.goals) as number_of_goals from players as p, player_assists_goals as a where  p.player_id=a.player_id and a.goals>2  group by(p.player_id) order by(number_of_goals) DESC;

#Query16
select country_name,population from country order by(population) DESC;

insert into country values('Australia',45,3,'varun');

drop table players;
select * from player_cards;
insert into player_cards values(271253,4,1);
































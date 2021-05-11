<h2>Introduction</h2>
<ul>
<li>The installation spawn a mysql docker container with db1 data base and employees table</li>
<li>my_sql_connector.py is a client app that uses mysql.connector to access mysql using sql</li>
<li>the image used to create the container is pre defined <a href='https://hub.docker.com/_/mysql'>mysql image</a> </li>
</ul>


<h2>Installation</h2>
<table>
  <tr>
    <th>Operations</th>
    <th>Description</th>
  </tr>
  <tr>
  <td>install connector for python</td>
  <td>pip install mysql-connector-python</td>
  </tr>
  <tr>
  <td>run the mysql container</td>
  <td>docker container run -d -p 3306:3306 --name my-mysql --env MYSQL_ROOT_PASSWORD=123abc mysql</td>
  </tr>
  <tr>
  <td>Enter the container command line</td>
  <td>docker container exec -it my-mysql bash</td>
  </tr>
  <tr>
  <td>Enter mysql as root</td>
  <td>mysql -u root -p123abc</td>
  </tr>
  <tr>
  <td>create database db1</td>
  <td>create database db1;</td>
  </tr>
  <tr>
  <td>attach to database db1</td>
  <td>use db1</td>
  </tr>
  <tr>
  <td>create a table in database db1</td>
  <td>create table employees(id int not null , name text , primary key (id));</td>
  </tr>
  <tr>
  <td>insert values to table</td>
  <td>insert into employees (id  , name) values (1 , 'Nathan');</td>
  </tr>
  <tr>
  <td>read values from table</td>
  <td>select * from employees;</td>
  </tr>
</table>


<h2>points of interest</h2>
<ul>
<li>all opertions done on the table are sql statements</li>
</ul>

<h2>future</h2>
<ul>
<li>most clean way to create database and table is by creating new mysql docker image based on mysql docker image. using sql script and run it via run in the docker file it is possible </li>
</ul>
show databases;

create database education_db;
use education_db;

select * from education;


create database univ_db;

create database univkm_db;
use univkm_db;
select * from univ_tbl;
select * from university_pred_kmeans;

create database amerdb;
use amerdb;
select * from ins_tbl;


create database wine_db;
use wine_db;
select * from wine_tbl;
select * from db_scan;

create database dbscan_db;
use dbscan_db;
select * from ins_tbl;
select * from ins_pred_kmeans;

create database univ_pca_db;
use univ_pca_db;
select * from university_clustering;
select * from university_pred_pca;

create database pca_db;
use pca_db;
select * from ins_tbl;
select * from pca_res;

create database svd_db;
use svd_db;
select * from ins_tbl;
select * from svd_res;

create database univ_svd_db;
use univ_svd_db;
select * from university_clustering;
select * from university_pred_svd;



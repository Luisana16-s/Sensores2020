# -*- coding: utf-8 -*-
"""
Created on Thu May  7 14:35:30 2020

@author: Acer
"""

import pandas as pd 
import pyodbc as p
#importar 
Base=pd.read_excel('features2.xlsx')
#print(Base)
B=Base.to_numpy()
Ba= pd.DataFrame(B, columns= ['Vector1','Vector2','Vector3','Vector4','Vector5','Vector6','Vector7','Vector8','Vector9','Vector10',
                              'Vector11','Vector12','Vector13','Vector14','Vector15','Vector16','Vector17','Vector18','Vector19','Vector20',
                              'Vector21','Vector22','Vector23','Vector24','Vector25','Vector26','Vector27','Vector28','Vector29','Vector30',
                              'Vector31','Vector32','Vector33','Vector34','Vector35','Vector36','Vector37','Vector38','Vector39','Vector40',
                              'Vector41','Vector42','Vector43','Vector44','Vector45','Vector46','Vector47','Vector48','Vector49','Vector50',
                              'Vector51','Vector52','Vector53','Vector54','Vector55','Vector56','Vector57','Vector58','Vector59','Vector60',
                              'Vector61','Vector62','Vector63','Vector64','Vector65','Vector66','Vector67','Vector68','Vector69','Vector70',
                              'Vector71','Vector72','Vector73','Vector74','Vector75','Vector76','Vector77','Vector78','Vector79','Vector80',
                              'Vector81','Vector82','Vector83','Vector84','Vector85','Vector86','Vector87','Vector88','Vector89','Vector90',
                              'Vector91','Vector92','Vector93','Vector94','Vector95','Vector96','Vector97','Vector98','Vector99','Vector100',
                              'Vector101','Vector102','Vector103','Vector104','Vector105','Vector106','Vector107','Vector108','Vector109','Vector110',
                              'Vector111','Vector112','Vector113','Vector114','Vector115','Vector116','Vector117','Vector118','Vector119','Vector120',
                              'Vector121','Vector122','Vector123','Vector124','Vector125','Vector126','Vector127','Vector128','Vector129','Vector130',
                              'Vector131','Vector132','Vector133','Vector134','Vector135','Vector136','Vector137','Vector138','Vector139','Vector140',
                              'Vector141','Vector142','Vector143','Vector144','Vector145','Vector146','Vector147','Vector148','Vector149','Vector150',
                              'Vector151','Vector152','Vector153','Vector154','Vector155','Vector156','Vector157','Vector158','Vector159','Vector160',
                              'Vector161','Vector162','Vector163','Vector164','Vector165','Vector166','Vector167','Vector168','Vector169','Vector170',
                              'Vector171','Vector172','Vector173','Vector174','Vector175','Vector176','Vector177','Vector178','Vector179','Vector180',
                              'Vector181','Vector182','Vector183','Vector184','Vector185','Vector186','Vector187','Vector188','Vector189','Vector190',
                              'Vector191','Vector192','Vector193','Vector194','Vector195','Vector196','Vector197','Vector198','Vector199','Vector200',
                              'Vector201','Vector202','Vector203','Vector204','Vector205','Vector206','Vector207','Vector208','Vector209','Vector210',
                              'Vector211','Vector212','Vector213','Vector214','Vector215','Vector216','Vector217','Vector218','Vector219','Vector220',
                              'Vector221','Vector222','Vector223','Vector224','Vector225','Vector226','Vector227','Vector228','Vector229','Vector230',
                              'Vector231','Vector232','Vector233','Vector234','Vector235','Vector236','Vector237','Vector238','Vector239','Vector240',
                              'Vector241','Vector242','Vector243','Vector244','Vector245','Vector246','Vector247','Vector248','Vector249','Vector250',
                              'Vector251','Vector252','Vector253','Vector254','Vector255','Vector256','Vector257','Clase'])
#print(Ba)
#conectar python a SQL
conn=p.connect('Driver={ODBC Driver 17 for SQL Server};'
               'SERVER=servidorlib-16.database.windows.net;'
               'DATABASE=Libros;'
               'UID=Luisa;'
               'PWD=300836Luchis;'
               'Trusted_Connection=no;')
cursor=conn.cursor()

#crear tabla en SQL desde phython
#cursor.execute('CREATE TABLE matrizC (Vector1 numeric(18,8),Vector2 numeric(18,8),Vector3 numeric(18,8),Clase int)')
cursor.execute('CREATE TABLE matrizD (Vector1 numeric(18,8),Vector2 numeric(18,8),Vector3 numeric(18,8), Vector4 numeric(18,8),Vector5 numeric(18,8),Vector6 numeric(18,8),Vector7 numeric(18,8),Vector8 numeric(18,8),Vector9 numeric(18,8),Vector10 numeric(18,8),Vector11 numeric(18,8),Vector12 numeric(18,8),Vector13 numeric(18,8), Vector14 numeric(18,8),Vector15 numeric(18,8),Vector16 numeric(18,8),Vector17 numeric(18,8),Vector18 numeric(18,8),Vector19 numeric(18,8),Vector20 numeric(18,8),Vector21 numeric(18,8),Vector22 numeric(18,8),Vector23 numeric(18,8), Vector24 numeric(18,8),Vector25 numeric(18,8),Vector26 numeric(18,8),Vector27 numeric(18,8),Vector28 numeric(18,8),Vector29 numeric(18,8),Vector30 numeric(18,8),Vector31 numeric(18,8),Vector32 numeric(18,8),Vector33 numeric(18,8), Vector34 numeric(18,8),Vector35 numeric(18,8),Vector36 numeric(18,8),Vector37 numeric(18,8),Vector38 numeric(18,8),Vector39 numeric(18,8),Vector40 numeric(18,8),Vector41 numeric(18,8),Vector42 numeric(18,8),Vector43 numeric(18,8), Vector44 numeric(18,8),Vector45 numeric(18,8),Vector46 numeric(18,8),Vector47 numeric(18,8),Vector48 numeric(18,8),Vector49 numeric(18,8),Vector50 numeric(18,8),Vector51 numeric(18,8),Vector52 numeric(18,8),Vector53 numeric(18,8), Vector54 numeric(18,8),Vector55 numeric(18,8),Vector56 numeric(18,8),Vector57 numeric(18,8),Vector58 numeric(18,8),Vector59 numeric(18,8),Vector60 numeric(18,8),Vector61 numeric(18,8),Vector62 numeric(18,8),Vector63 numeric(18,8), Vector64 numeric(18,8),Vector65 numeric(18,8),Vector66 numeric(18,8),Vector67 numeric(18,8),Vector68 numeric(18,8),Vector69 numeric(18,8),Vector70 numeric(18,8),Vector71 numeric(18,8),Vector72 numeric(18,8),Vector73 numeric(18,8), Vector74 numeric(18,8),Vector75 numeric(18,8),Vector76 numeric(18,8),Vector77 numeric(18,8),Vector78 numeric(18,8),Vector79 numeric(18,8),Vector80 numeric(18,8),Vector81 numeric(18,8),Vector82 numeric(18,8),Vector83 numeric(18,8), Vector84 numeric(18,8),Vector85 numeric(18,8),Vector86 numeric(18,8),Vector87 numeric(18,8),Vector88 numeric(18,8),Vector89 numeric(18,8),Vector90 numeric(18,8),Vector91 numeric(18,8),Vector92 numeric(18,8),Vector93 numeric(18,8), Vector94 numeric(18,8),Vector95 numeric(18,8),Vector96 numeric(18,8),Vector97 numeric(18,8),Vector98 numeric(18,8),Vector99 numeric(18,8),Vector100 numeric(18,8),Vector101 numeric(18,8),Vector102 numeric(18,8),Vector103 numeric(18,8), Vector104 numeric(18,8),Vector105 numeric(18,8),Vector106 numeric(18,8),Vector107 numeric(18,8),Vector108 numeric(18,8),Vector109 numeric(18,8),Vector110 numeric(18,8),Vector111 numeric(18,8),Vector112 numeric(18,8),Vector113 numeric(18,8), Vector114 numeric(18,8),Vector115 numeric(18,8),Vector116 numeric(18,8),Vector117 numeric(18,8),Vector118 numeric(18,8),Vector119 numeric(18,8),Vector120 numeric(18,8),Vector121 numeric(18,8),Vector122 numeric(18,8),Vector123 numeric(18,8), Vector124 numeric(18,8),Vector125 numeric(18,8),Vector126 numeric(18,8),Vector127 numeric(18,8),Vector128 numeric(18,8),Vector129 numeric(18,8),Vector130 numeric(18,8),Vector131 numeric(18,8),Vector132 numeric(18,8),Vector133 numeric(18,8), Vector134 numeric(18,8),Vector135 numeric(18,8),Vector136 numeric(18,8),Vector137 numeric(18,8),Vector138 numeric(18,8),Vector139 numeric(18,8),Vector140 numeric(18,8),Vector141 numeric(18,8),Vector142 numeric(18,8),Vector143 numeric(18,8), Vector144 numeric(18,8),Vector145 numeric(18,8),Vector146 numeric(18,8),Vector147 numeric(18,8),Vector148 numeric(18,8),Vector149 numeric(18,8),Vector150 numeric(18,8),Vector151 numeric(18,8),Vector152 numeric(18,8),Vector153 numeric(18,8), Vector154 numeric(18,8),Vector155 numeric(18,8),Vector156 numeric(18,8),Vector157 numeric(18,8),Vector158 numeric(18,8),Vector159 numeric(18,8),Vector160 numeric(18,8),Vector161 numeric(18,8),Vector162 numeric(18,8),Vector163 numeric(18,8), Vector164 numeric(18,8),Vector165 numeric(18,8),Vector166 numeric(18,8),Vector167 numeric(18,8),Vector168 numeric(18,8),Vector169 numeric(18,8),Vector170 numeric(18,8),Vector171 numeric(18,8),Vector172 numeric(18,8),Vector173 numeric(18,8), Vector174 numeric(18,8),Vector175 numeric(18,8),Vector176 numeric(18,8),Vector177 numeric(18,8),Vector178 numeric(18,8),Vector179 numeric(18,8),Vector180 numeric(18,8),Vector181 numeric(18,8),Vector182 numeric(18,8),Vector183 numeric(18,8), Vector184 numeric(18,8),Vector185 numeric(18,8),Vector186 numeric(18,8),Vector187 numeric(18,8),Vector188 numeric(18,8),Vector189 numeric(18,8),Vector190 numeric(18,8),Vector191 numeric(18,8),Vector192 numeric(18,8),Vector193 numeric(18,8), Vector194 numeric(18,8),Vector195 numeric(18,8),Vector196 numeric(18,8),Vector197 numeric(18,8),Vector198 numeric(18,8),Vector199 numeric(18,8),Vector200 numeric(18,8),Vector201 numeric(18,8),Vector202 numeric(18,8),Vector203 numeric(18,8), Vector204 numeric(18,8),Vector205 numeric(18,8),Vector206 numeric(18,8),Vector207 numeric(18,8),Vector208 numeric(18,8),Vector209 numeric(18,8),Vector210 numeric(18,8),Vector211 numeric(18,8),Vector212 numeric(18,8),Vector213 numeric(18,8), Vector214 numeric(18,8),Vector215 numeric(18,8),Vector216 numeric(18,8),Vector217 numeric(18,8),Vector218 numeric(18,8),Vector219 numeric(18,8),Vector220 numeric(18,8),Vector221 numeric(18,8),Vector222 numeric(18,8),Vector223 numeric(18,8), Vector224 numeric(18,8),Vector225 numeric(18,8),Vector226 numeric(18,8),Vector227 numeric(18,8),Vector228 numeric(18,8),Vector229 numeric(18,8),Vector230 numeric(18,8),Vector231 numeric(18,8),Vector232 numeric(18,8),Vector233 numeric(18,8), Vector234 numeric(18,8),Vector235 numeric(18,8),Vector236 numeric(18,8),Vector237 numeric(18,8),Vector238 numeric(18,8),Vector239 numeric(18,8),Vector240 numeric(18,8),Vector241 numeric(18,8),Vector242 numeric(18,8),Vector243 numeric(18,8), Vector244 numeric(18,8),Vector245 numeric(18,8),Vector246 numeric(18,8),Vector247 numeric(18,8),Vector248 numeric(18,8),Vector249 numeric(18,8),Vector250 numeric(18,8),Vector251 numeric(18,8),Vector252 numeric(18,8),Vector253 numeric(18,8), Vector254 numeric(18,8),Vector255 numeric(18,8),Vector256 numeric(18,8),Vector257 numeric(18,8),Clase int)')   
 

for row in Ba.itertuples():
    cursor.execute("""
                INSERT INTO Libros.dbo.matrizD (Vector1,Vector2,Vector3,Vector4,Vector5,Vector6,Vector7,Vector8,Vector9,Vector10,
                                                Vector11,Vector12,Vector13,Vector14,Vector15,Vector16,Vector17,Vector18,Vector19,Vector20,
                                                Vector21,Vector22,Vector23,Vector24,Vector25,Vector26,Vector27,Vector28,Vector29,Vector30,
                                                Vector31,Vector32,Vector33,Vector34,Vector35,Vector36,Vector37,Vector38,Vector39,Vector40,
                                                Vector41,Vector42,Vector43,Vector44,Vector45,Vector46,Vector47,Vector48,Vector49,Vector50,
                                                Vector51,Vector52,Vector53,Vector54,Vector55,Vector56,Vector57,Vector58,Vector59,Vector60,
                                                Vector61,Vector62,Vector63,Vector64,Vector65,Vector66,Vector67,Vector68,Vector69,Vector70,
                                                Vector71,Vector72,Vector73,Vector74,Vector75,Vector76,Vector77,Vector78,Vector79,Vector80,
                                                Vector81,Vector82,Vector83,Vector84,Vector85,Vector86,Vector87,Vector88,Vector89,Vector90,
                                                Vector91,Vector92,Vector93,Vector94,Vector95,Vector96,Vector97,Vector98,Vector99,Vector100,
                                                Vector101,Vector102,Vector103,Vector104,Vector105,Vector106,Vector107,Vector108,Vector109,Vector110,
                                                Vector111,Vector112,Vector113,Vector114,Vector115,Vector116,Vector117,Vector118,Vector119,Vector120,
                                                Vector121,Vector122,Vector123,Vector124,Vector125,Vector126,Vector127,Vector128,Vector129,Vector130,
                                                Vector131,Vector132,Vector133,Vector134,Vector135,Vector136,Vector137,Vector138,Vector139,Vector140,
                                                Vector141,Vector142,Vector143,Vector144,Vector145,Vector146,Vector147,Vector148,Vector149,Vector150,
                                                Vector151,Vector152,Vector153,Vector154,Vector155,Vector156,Vector157,Vector158,Vector159,Vector160,
                                                Vector161,Vector162,Vector163,Vector164,Vector165,Vector166,Vector167,Vector168,Vector169,Vector170,
                                                Vector171,Vector172,Vector173,Vector174,Vector175,Vector176,Vector177,Vector178,Vector179,Vector180,
                                                Vector181,Vector182,Vector183,Vector184,Vector185,Vector186,Vector187,Vector188,Vector189,Vector190,
                                                Vector191,Vector192,Vector193,Vector194,Vector195,Vector196,Vector197,Vector198,Vector199,Vector200,
                                                Vector201,Vector202,Vector203,Vector204,Vector205,Vector206,Vector207,Vector208,Vector209,Vector210,
                                                Vector211,Vector212,Vector213,Vector214,Vector215,Vector216,Vector217,Vector218,Vector219,Vector220,
                                                Vector221,Vector222,Vector223,Vector224,Vector225,Vector226,Vector227,Vector228,Vector229,Vector230,
                                                Vector231,Vector232,Vector233,Vector234,Vector235,Vector236,Vector237,Vector238,Vector239,Vector240,
                                                Vector241,Vector242,Vector243,Vector244,Vector245,Vector246,Vector247,Vector248,Vector249,Vector250,
                                                Vector251,Vector252,Vector253,Vector254,Vector255,Vector256,Vector257,Clase)
                VALUES (?,?,?,?,?,?,?,?,?,?,
                        ?,?,?,?,?,?,?,?,?,?,
                        ?,?,?,?,?,?,?,?,?,?,
                        ?,?,?,?,?,?,?,?,?,?,
                        ?,?,?,?,?,?,?,?,?,?,
                        ?,?,?,?,?,?,?,?,?,?,
                        ?,?,?,?,?,?,?,?,?,?,
                        ?,?,?,?,?,?,?,?,?,?,
                        ?,?,?,?,?,?,?,?,?,?,
                        ?,?,?,?,?,?,?,?,?,?,
                        ?,?,?,?,?,?,?,?,?,?,
                        ?,?,?,?,?,?,?,?,?,?,
                        ?,?,?,?,?,?,?,?,?,?,
                        ?,?,?,?,?,?,?,?,?,?,
                        ?,?,?,?,?,?,?,?,?,?,
                        ?,?,?,?,?,?,?,?,?,?,
                        ?,?,?,?,?,?,?,?,?,?,
                        ?,?,?,?,?,?,?,?,?,?,
                        ?,?,?,?,?,?,?,?,?,?,
                        ?,?,?,?,?,?,?,?,?,?,
                        ?,?,?,?,?,?,?,?,?,?,
                        ?,?,?,?,?,?,?,?,?,?,
                        ?,?,?,?,?,?,?,?,?,?,
                        ?,?,?,?,?,?,?,?,?,?,
                        ?,?,?,?,?,?,?,?,?,?,
                        ?,?,?,?,?,?,?,?)
                """,
                row.Vector1,row.Vector2,row.Vector3,row.Vector4,row.Vector5,row.Vector6,row.Vector7,row.Vector8,row.Vector9,row.Vector10,
                row.Vector11,row.Vector12,row.Vector13,row.Vector14,row.Vector15,row.Vector16,row.Vector17,row.Vector18,row.Vector19,row.Vector20,
                row.Vector21,row.Vector22,row.Vector23,row.Vector24,row.Vector25,row.Vector26,row.Vector27,row.Vector28,row.Vector29,row.Vector30,
                row.Vector31,row.Vector32,row.Vector33,row.Vector34,row.Vector35,row.Vector36,row.Vector37,row.Vector38,row.Vector39,row.Vector40,
                row.Vector41,row.Vector42,row.Vector43,row.Vector44,row.Vector45,row.Vector46,row.Vector47,row.Vector48,row.Vector49,row.Vector50,
                row.Vector51,row.Vector52,row.Vector53,row.Vector54,row.Vector55,row.Vector56,row.Vector57,row.Vector58,row.Vector59,row.Vector60,
                row.Vector61,row.Vector62,row.Vector63,row.Vector64,row.Vector65,row.Vector66,row.Vector67,row.Vector68,row.Vector69,row.Vector70,
                row.Vector71,row.Vector72,row.Vector73,row.Vector74,row.Vector75,row.Vector76,row.Vector77,row.Vector78,row.Vector79,row.Vector80,
                row.Vector81,row.Vector82,row.Vector83,row.Vector84,row.Vector85,row.Vector86,row.Vector87,row.Vector88,row.Vector89,row.Vector90,
                row.Vector91,row.Vector92,row.Vector93,row.Vector94,row.Vector95,row.Vector96,row.Vector97,row.Vector98,row.Vector99,row.Vector100,
                row.Vector101,row.Vector102,row.Vector103,row.Vector104,row.Vector105,row.Vector106,row.Vector107,row.Vector108,row.Vector109,row.Vector110,
                row.Vector111,row.Vector112,row.Vector113,row.Vector114,row.Vector115,row.Vector116,row.Vector117,row.Vector118,row.Vector119,row.Vector120,
                row.Vector121,row.Vector122,row.Vector123,row.Vector124,row.Vector125,row.Vector126,row.Vector127,row.Vector128,row.Vector129,row.Vector130,
                row.Vector131,row.Vector132,row.Vector133,row.Vector134,row.Vector135,row.Vector136,row.Vector137,row.Vector138,row.Vector139,row.Vector140,
                row.Vector141,row.Vector142,row.Vector143,row.Vector144,row.Vector145,row.Vector146,row.Vector147,row.Vector148,row.Vector149,row.Vector150,
                row.Vector151,row.Vector152,row.Vector153,row.Vector154,row.Vector155,row.Vector156,row.Vector157,row.Vector158,row.Vector159,row.Vector160,
                row.Vector161,row.Vector162,row.Vector163,row.Vector164,row.Vector165,row.Vector166,row.Vector167,row.Vector168,row.Vector169,row.Vector170,
                row.Vector171,row.Vector172,row.Vector173,row.Vector174,row.Vector175,row.Vector176,row.Vector177,row.Vector178,row.Vector179,row.Vector180,
                row.Vector181,row.Vector182,row.Vector183,row.Vector184,row.Vector185,row.Vector186,row.Vector187,row.Vector188,row.Vector189,row.Vector190,
                row.Vector191,row.Vector192,row.Vector193,row.Vector194,row.Vector195,row.Vector196,row.Vector197,row.Vector198,row.Vector199,row.Vector200,
                row.Vector201,row.Vector202,row.Vector203,row.Vector204,row.Vector205,row.Vector206,row.Vector207,row.Vector208,row.Vector209,row.Vector210,
                row.Vector211,row.Vector212,row.Vector213,row.Vector214,row.Vector215,row.Vector216,row.Vector217,row.Vector218,row.Vector219,row.Vector220,
                row.Vector221,row.Vector222,row.Vector223,row.Vector224,row.Vector225,row.Vector226,row.Vector227,row.Vector228,row.Vector229,row.Vector230,
                row.Vector231,row.Vector232,row.Vector233,row.Vector234,row.Vector235,row.Vector236,row.Vector237,row.Vector238,row.Vector239,row.Vector240,
                row.Vector241,row.Vector242,row.Vector243,row.Vector244,row.Vector245,row.Vector246,row.Vector247,row.Vector248,row.Vector249,row.Vector250,
                row.Vector251,row.Vector252,row.Vector253,row.Vector254,row.Vector255,row.Vector256,row.Vector257,row.Clase
                )
conn.commit()

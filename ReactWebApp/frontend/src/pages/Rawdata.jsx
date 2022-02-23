import React, {useState} from 'react'

import * as Tables from '../components/table'

const API = process.env.REACT_APP_API;

const default_table_head = [
    '',
    'group',
    'country',
    'country_code',
    'incidents_sent',
]

const renderHead = (item, index) => <th key={index}>{item}</th>

const renderBody = (item, index) => (
    <tr key={index}>
        <td>{item.id}</td>
        <td>{item.group_name}</td>
        <td>{item.country}</td>
        <td>{item.country_code}</td>
        <td>{item.incidents_sent}</td>
    </tr>
)

const Rawdata = () => {

    const [collection, setCollection] = useState('Table')

    const [table_data, setTable] = useState([
        {
            "_id": "613b25bb4ee0156be0554fb3",
            "country": "China",
            "country_code": "CHN",
            "group_name": "APT1",
            "incidents_sent": 5,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2016",
                "2018",
                "2016",
                "2014",
                "2014"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fb4",
            "country": "Iran",
            "country_code": "IRN",
            "group_name": "AjaxSecurityTeam",
            "incidents_sent": 5,
            "latitude": "32.0000",
            "longitude": "53.0000",
            "year_list": [
                "2017",
                "2015",
                "2014",
                "2013",
                "2015"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fb5",
            "country": "China",
            "country_code": "CHN",
            "group_name": "APT18",
            "incidents_sent": 6,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2016",
                "2015",
                "2016",
                "2015",
                "2017",
                "2014"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fb6",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "APT28",
            "incidents_sent": 46,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2018",
                "2020",
                "2016",
                "2018",
                "2016",
                "2018",
                "2017",
                "2020",
                "2015",
                "2015",
                "2016",
                "2015",
                "2016",
                "2018",
                "2015",
                "2018",
                "2017",
                "2019",
                "2018",
                "2015",
                "2015",
                "2017",
                "2015",
                "2017",
                "2016",
                "2018",
                "2016",
                "2020",
                "2020",
                "2018",
                "2020",
                "2017",
                "2017",
                "2016",
                "2017",
                "2016",
                "2018",
                "2018",
                "2016",
                "2017",
                "2017",
                "2018",
                "2019",
                "2016",
                "2018",
                "2017"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fb7",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "APT29",
            "incidents_sent": 33,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2016",
                "2021",
                "2021",
                "2016",
                "2015",
                "2017",
                "2016",
                "2021",
                "2020",
                "2018",
                "2016",
                "2019",
                "2018",
                "2020",
                "2021",
                "2021",
                "2020",
                "2015",
                "2020",
                "2020",
                "2020",
                "2017",
                "2020",
                "2020",
                "2021",
                "2020",
                "2015",
                "2021",
                "2021",
                "2020",
                "2021",
                "2020",
                "2021"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fb8",
            "country": "China",
            "country_code": "CHN",
            "group_name": "APT3",
            "incidents_sent": 11,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2015",
                "2016",
                "2018",
                "2014",
                "2017",
                "2017",
                "2014",
                "2015",
                "2017",
                "2012",
                "2014"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fb9",
            "country": "Saudi Arabia",
            "country_code": "SAU",
            "group_name": "APT33",
            "incidents_sent": 5,
            "latitude": "25.0000",
            "longitude": "45.0000",
            "year_list": [
                "2019",
                "2018",
                "2017",
                "2017",
                "2020"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fba",
            "country": "North Korea",
            "country_code": "PRK",
            "group_name": "APT38",
            "incidents_sent": 3,
            "latitude": "37.0000",
            "longitude": "127.5000",
            "year_list": [
                "2017",
                "2018",
                "2017"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fbb",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "CobaltGroup",
            "incidents_sent": 13,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2017",
                "2018",
                "2018",
                "2017",
                "2018",
                "2018",
                "2017",
                "2017",
                "2017",
                "2018",
                "2018",
                "2016",
                "2020"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fbc",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "FIN7",
            "incidents_sent": 30,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2019",
                "2017",
                "2017",
                "2017",
                "2017",
                "2019",
                "2020",
                "2017",
                "2017",
                "2017",
                "2018",
                "2020",
                "2018",
                "2019",
                "2017",
                "2017",
                "2017",
                "2019",
                "2020",
                "2018",
                "2018",
                "2020",
                "2018",
                "2019",
                "2018",
                "2017",
                "2017",
                "2017",
                "2020",
                "2017"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fbd",
            "country": "Australia",
            "country_code": "AUS",
            "group_name": "FoxKitten",
            "incidents_sent": 6,
            "latitude": "-27.0000",
            "longitude": "133.0000",
            "year_list": [
                "2020",
                "2020",
                "2020",
                "2020",
                "2020",
                "2020"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fbe",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "GamaredonGroup",
            "incidents_sent": 3,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2017",
                "2020",
                "2020"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fbf",
            "country": "United States",
            "country_code": "USA",
            "group_name": "Kimsuky",
            "incidents_sent": 10,
            "latitude": "38.0000",
            "longitude": "-97.0000",
            "year_list": [
                "2019",
                "2018",
                "2019",
                "2020",
                "2020",
                "2020",
                "2013",
                "2020",
                "2020",
                "2019"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fc0",
            "country": "North Korea",
            "country_code": "PRK",
            "group_name": "LazarusGroup",
            "incidents_sent": 38,
            "latitude": "37.0000",
            "longitude": "127.5000",
            "year_list": [
                "2018",
                "2018",
                "2017",
                "2018",
                "2017",
                "2016",
                "2018",
                "2018",
                "2017",
                "2020",
                "2018",
                "2021",
                "2017",
                "2017",
                "2016",
                "2020",
                "2018",
                "2017",
                "2016",
                "2020",
                "2020",
                "2017",
                "2018",
                "2020",
                "2018",
                "2019",
                "2019",
                "2017",
                "2018",
                "2016",
                "2018",
                "2018",
                "2020",
                "2017",
                "2017",
                "2016",
                "2020",
                "2017"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fc1",
            "country": "Iran",
            "country_code": "IRN",
            "group_name": "MagicHound",
            "incidents_sent": 13,
            "latitude": "32.0000",
            "longitude": "53.0000",
            "year_list": [
                "2017",
                "2014",
                "2019",
                "2018",
                "2019",
                "2017",
                "2020",
                "2017",
                "2020",
                "2021",
                "2019",
                "2017",
                "2020"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fc2",
            "country": "Iran",
            "country_code": "IRN",
            "group_name": "MuddyWater",
            "incidents_sent": 13,
            "latitude": "32.0000",
            "longitude": "53.0000",
            "year_list": [
                "2019",
                "2017",
                "2019",
                "2018",
                "2017",
                "2018",
                "2019",
                "2017",
                "2018",
                "2018",
                "2021",
                "2021",
                "2018"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fc3",
            "country": "Iran",
            "country_code": "IRN",
            "group_name": "OilRig",
            "incidents_sent": 22,
            "latitude": "32.0000",
            "longitude": "53.0000",
            "year_list": [
                "2017",
                "2016",
                "2021",
                "2017",
                "2017",
                "2017",
                "2019",
                "2018",
                "2018",
                "2017",
                "2018",
                "2018",
                "2016",
                "2017",
                "2017",
                "2020",
                "2018",
                "2016",
                "2018",
                "2018",
                "2020",
                "2019"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fc4",
            "country": "Cambodia",
            "country_code": "KHM",
            "group_name": "APT32",
            "incidents_sent": 14,
            "latitude": "13.0000",
            "longitude": "105.0000",
            "year_list": [
                "2019",
                "2019",
                "2021",
                "2018",
                "2020",
                "2017",
                "2017",
                "2020",
                "2017",
                "2018",
                "2017",
                "2017",
                "2017",
                "2017"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fc5",
            "country": "China",
            "country_code": "CHN",
            "group_name": "APT37",
            "incidents_sent": 8,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2017",
                "2018",
                "2018",
                "2016",
                "2017",
                "2019",
                "2018",
                "2018"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fc6",
            "country": "China",
            "country_code": "CHN",
            "group_name": "APT41",
            "incidents_sent": 6,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2019",
                "2019",
                "2020",
                "2020",
                "2021",
                "2019"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fc7",
            "country": "Japan",
            "country_code": "JPN",
            "group_name": "DragonOK",
            "incidents_sent": 5,
            "latitude": "36.0000",
            "longitude": "138.0000",
            "year_list": [
                "2014",
                "2015",
                "2016",
                "2015",
                "2017"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fc8",
            "country": "United States",
            "country_code": "USA",
            "group_name": "Equation",
            "incidents_sent": 2,
            "latitude": "38.0000",
            "longitude": "-97.0000",
            "year_list": [
                "2012",
                "2015"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fc9",
            "country": "United States",
            "country_code": "USA",
            "group_name": "Inception",
            "incidents_sent": 4,
            "latitude": "38.0000",
            "longitude": "-97.0000",
            "year_list": [
                "2014",
                "2018",
                "2018",
                "2019"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fca",
            "country": "Colombia",
            "country_code": "COL",
            "group_name": "APT-C-36",
            "incidents_sent": 1,
            "latitude": "4.0000",
            "longitude": "-72.0000",
            "year_list": [
                "2019"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fcb",
            "country": "China",
            "country_code": "CHN",
            "group_name": "APT17",
            "incidents_sent": 1,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2015"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fcc",
            "country": "China",
            "country_code": "CHN",
            "group_name": "APT19",
            "incidents_sent": 6,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2016",
                "ACSC",
                "2018",
                "2015",
                "2017",
                "2016"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fcd",
            "country": "China",
            "country_code": "CHN",
            "group_name": "APT30",
            "incidents_sent": 2,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2015",
                "2015"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fce",
            "country": "Iran",
            "country_code": "IRN",
            "group_name": "APT39",
            "incidents_sent": 11,
            "latitude": "32.0000",
            "longitude": "53.0000",
            "year_list": [
                "2020",
                "2019",
                "2015",
                "2020",
                "2020",
                "2020",
                "2019",
                "2018",
                "2019",
                "2020",
                "2019"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fcf",
            "country": "Hong Kong",
            "country_code": "HKG",
            "group_name": "BlackTech",
            "incidents_sent": 4,
            "latitude": "22.2500",
            "longitude": "114.1667",
            "year_list": [
                "2019",
                "2017",
                "2018",
                "2018"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fd0",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Chimera",
            "incidents_sent": 4,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2021",
                "2020",
                "2018",
                "2019"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fd1",
            "country": "China",
            "country_code": "CHN",
            "group_name": "DeepPanda",
            "incidents_sent": 7,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2017",
                "2015",
                "2014",
                "2014",
                "2014",
                "2015",
                "2016"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fd2",
            "country": "Japan",
            "country_code": "JPN",
            "group_name": "DustStorm",
            "incidents_sent": 1,
            "latitude": "36.0000",
            "longitude": "138.0000",
            "year_list": [
                "2016"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fd3",
            "country": "China",
            "country_code": "CHN",
            "group_name": "HAFNIUM",
            "incidents_sent": 3,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2021",
                "2021",
                "2021"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fd4",
            "country": "China",
            "country_code": "CHN",
            "group_name": "LotusBlossom",
            "incidents_sent": 5,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2016",
                "2018",
                "2015",
                "2015",
                "2015"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fd5",
            "country": "Japan",
            "country_code": "JPN",
            "group_name": "menuPass",
            "incidents_sent": 12,
            "latitude": "36.0000",
            "longitude": "138.0000",
            "year_list": [
                "2017",
                "2017",
                "2018",
                "2017",
                "2020",
                "2013",
                "2015",
                "2018",
                "2014",
                "2018",
                "2017",
                "2019"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fd6",
            "country": "China",
            "country_code": "CHN",
            "group_name": "APT16",
            "incidents_sent": 1,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2015"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fd7",
            "country": "Japan",
            "country_code": "JPN",
            "group_name": "BRONZEBUTLER",
            "incidents_sent": 5,
            "latitude": "36.0000",
            "longitude": "138.0000",
            "year_list": [
                "2017",
                "2017",
                "2019",
                "2021",
                "2016"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fd8",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "Carbanak",
            "incidents_sent": 7,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2015",
                "2017",
                "2020",
                "2016",
                "2014",
                "2015",
                "2017"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fd9",
            "country": "South Korea",
            "country_code": "KOR",
            "group_name": "Darkhotel",
            "incidents_sent": 7,
            "latitude": "37.0000",
            "longitude": "127.5000",
            "year_list": [
                "2020",
                "2016",
                "2015",
                "2016",
                "2015",
                "2014",
                "2016"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fda",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Dragonfly2.0",
            "incidents_sent": 10,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2017",
                "2018",
                "2017",
                "2014",
                "2019",
                "2017",
                "2019",
                "2020",
                "2017",
                "2020"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fdb",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Naikon",
            "incidents_sent": 4,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2015",
                "2020",
                "2015",
                "DGI"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fdc",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Axiom",
            "incidents_sent": 6,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2015",
                "2014",
                "2014",
                "2013",
                "2014",
                "2015"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fdd",
            "country": "Iran",
            "country_code": "IRN",
            "group_name": "Cleaver",
            "incidents_sent": 2,
            "latitude": "32.0000",
            "longitude": "53.0000",
            "year_list": [
                "2015",
                "2014"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fde",
            "country": "Germany",
            "country_code": "DEU",
            "group_name": "CopyKittens",
            "incidents_sent": 3,
            "latitude": "51.0000",
            "longitude": "9.0000",
            "year_list": [
                "2017",
                "2015",
                "2017"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fdf",
            "country": "Romania",
            "country_code": "ROM",
            "group_name": "FIN4",
            "incidents_sent": 3,
            "latitude": "46.0000",
            "longitude": "25.0000",
            "year_list": [
                "2014",
                "2014",
                "2014"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fe0",
            "country": "China",
            "country_code": "CHN",
            "group_name": "GALLIUM",
            "incidents_sent": 2,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2019",
                "2019"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fe1",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "GCMAN",
            "incidents_sent": 1,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2016"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fe2",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Leviathan",
            "incidents_sent": 3,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2017",
                "2018",
                "2019"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fe3",
            "country": "United States",
            "country_code": "USA",
            "group_name": "Molerats",
            "incidents_sent": 6,
            "latitude": "38.0000",
            "longitude": "-97.0000",
            "year_list": [
                "2016",
                "2016",
                "2013",
                "2020",
                "2019",
                "2020"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fe4",
            "country": "China",
            "country_code": "CHN",
            "group_name": "MustangPanda",
            "incidents_sent": 7,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2019",
                "2020",
                "2020",
                "2018",
                "2019",
                "2020",
                "2021"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fe5",
            "country": "China",
            "country_code": "CHN",
            "group_name": "admin@338",
            "incidents_sent": 1,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2015"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fe6",
            "country": "China",
            "country_code": "CHN",
            "group_name": "APT12",
            "incidents_sent": 4,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2013",
                "2012",
                "2014",
                "2013"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fe7",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Dragonfly",
            "incidents_sent": 7,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2017",
                "2014",
                "2019",
                "2019",
                "2020",
                "2019",
                "2017"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fe8",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Higaisa",
            "incidents_sent": 3,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2020",
                "2020",
                "2020"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fe9",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Ke3chang",
            "incidents_sent": 4,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2018",
                "2014",
                "2018",
                "2019"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fea",
            "country": "Argentina",
            "country_code": "ARG",
            "group_name": "Honeybee",
            "incidents_sent": 1,
            "latitude": "-34.0000",
            "longitude": "-64.0000",
            "year_list": [
                "2018"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554feb",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "IndrikSpider",
            "incidents_sent": 1,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2018"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fec",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Mofang",
            "incidents_sent": 1,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2016"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fed",
            "country": "China",
            "country_code": "CHN",
            "group_name": "NightDragon",
            "incidents_sent": 1,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2011"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fee",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Elderwood",
            "incidents_sent": 4,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2012",
                "2012",
                "2012",
                "2012"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fef",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Group5",
            "incidents_sent": 1,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2016"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554ff0",
            "country": "Lebanon",
            "country_code": "LBN",
            "group_name": "DarkCaracal",
            "incidents_sent": 1,
            "latitude": "33.8333",
            "longitude": "35.8333",
            "year_list": [
                "2018"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554ff1",
            "country": "Pakistan",
            "country_code": "PAK",
            "group_name": "GorgonGroup",
            "incidents_sent": 1,
            "latitude": "30.0000",
            "longitude": "70.0000",
            "year_list": [
                "2018"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554ff2",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Moafee",
            "incidents_sent": 1,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2014"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554ff3",
            "country": "India",
            "country_code": "IND",
            "group_name": "Patchwork",
            "incidents_sent": 9,
            "latitude": "20.0000",
            "longitude": "77.0000",
            "year_list": [
                "2020",
                "2013",
                "2016",
                "2018",
                "2017",
                "2018",
                "2016",
                "2016",
                "2016"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554ff4",
            "country": "Georgia",
            "country_code": "GEO",
            "group_name": "SandwormTeam",
            "incidents_sent": 23,
            "latitude": "42.0000",
            "longitude": "43.5000",
            "year_list": [
                "2020",
                "2018",
                "2017",
                "2016",
                "2018",
                "2016",
                "2016",
                "2016",
                "2020",
                "2020",
                "2021",
                "2020",
                "2013",
                "2014",
                "2014",
                "2017",
                "2018",
                "2017",
                "2019",
                "2019",
                "2020",
                "2017",
                "2014"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554ff5",
            "country": "Afghanistan",
            "country_code": "AFG",
            "group_name": "Sidewinder",
            "incidents_sent": 5,
            "latitude": "33.0000",
            "longitude": "65.0000",
            "year_list": [
                "2020",
                "2020",
                "2018",
                "2020",
                "2021"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554ff6",
            "country": "Iran",
            "country_code": "IRN",
            "group_name": "SilentLibrarian",
            "incidents_sent": 6,
            "latitude": "32.0000",
            "longitude": "53.0000",
            "year_list": [
                "2019",
                "2019",
                "2018",
                "2018",
                "2020",
                "2018"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554ff7",
            "country": "Belgium",
            "country_code": "BEL",
            "group_name": "Strider",
            "incidents_sent": 3,
            "latitude": "50.8333",
            "longitude": "4.0000",
            "year_list": [
                "2016",
                "2016",
                "2016"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554ff8",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "TEMP.Veles",
            "incidents_sent": 10,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2019",
                "2018",
                "2019",
                "2019",
                "2019",
                "2018",
                "2017",
                "2019",
                "2014",
                "2017"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554ff9",
            "country": "China",
            "country_code": "CHN",
            "group_name": "APT 12, Numbered Panda",
            "incidents_sent": 6,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2011",
                "2012",
                "2016",
                "2009",
                "2016",
                "2011"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554ffa",
            "country": "China",
            "country_code": "CHN",
            "group_name": "APT 17, Deputy Dog, Elderwood, Sneaky Panda",
            "incidents_sent": 10,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2009",
                "2012",
                "2010",
                "2009",
                "2013",
                "2017",
                "2014",
                "2012",
                "2013",
                "2017"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554ffb",
            "country": "China",
            "country_code": "CHN",
            "group_name": "APT 19, Deep Panda, C0d0so0",
            "incidents_sent": 15,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2014",
                "2014",
                "2014",
                "2014",
                "2014",
                "2014",
                "2015",
                "2017",
                "2013",
                "2015",
                "2015",
                "2014",
                "2015",
                "2016",
                "2017"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554ffc",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "APT 29, Cozy Bear, The Dukes",
            "incidents_sent": 15,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2016",
                "2016",
                "2016",
                "2014",
                "2017",
                "2015",
                "2017",
                "2013",
                "2020",
                "2017",
                "2013",
                "2018",
                "2021",
                "2013",
                "2019"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554ffd",
            "country": "Vietnam",
            "country_code": "VNM",
            "group_name": "APT 32, OceanLotus, SeaLotus",
            "incidents_sent": 25,
            "latitude": "16.0000",
            "longitude": "106.0000",
            "year_list": [
                "2016",
                "2017",
                "2017",
                "2018",
                "2019",
                "2020",
                "2020",
                "2015",
                "2018",
                "2018",
                "2018",
                "2020",
                "2014",
                "2018",
                "2019",
                "2018",
                "2014",
                "2019",
                "2019",
                "2017",
                "2018",
                "2019",
                "2014",
                "2017",
                "2020"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554ffe",
            "country": "China",
            "country_code": "CHN",
            "group_name": "APT 41",
            "incidents_sent": 14,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2020",
                "2019",
                "2018",
                "2019",
                "2019",
                "2020",
                "2017",
                "2020",
                "2019",
                "2021",
                "2016",
                "2020",
                "2019",
                "2020"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0554fff",
            "country": "Middle East",
            "country_code": "MEA",
            "group_name": "Bahamut",
            "incidents_sent": 5,
            "latitude": "35.8333",
            "longitude": "14.5833",
            "year_list": [
                "2018",
                "2018",
                "2016",
                "2020",
                "2017"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555000",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "Berserk Bear, Dragonfly 2.0",
            "incidents_sent": 5,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2017",
                "2017",
                "2017",
                "2015",
                "2017"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555001",
            "country": "China",
            "country_code": "CHN",
            "group_name": "BlackTech, Circuit Panda, Radio Panda",
            "incidents_sent": 6,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2020",
                "2019",
                "2010",
                "2020",
                "2018",
                "2019"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555002",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Bronze Butler, Tick, RedBaldNight, Stalker Panda",
            "incidents_sent": 7,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2015",
                "2019",
                "2018",
                "2017",
                "2019",
                "2021",
                "2017"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555003",
            "country": "Ukraine",
            "country_code": "UKR",
            "group_name": "Carbanak, Anunak",
            "incidents_sent": 15,
            "latitude": "49.0000",
            "longitude": "32.0000",
            "year_list": [
                "2020",
                "2021",
                "2021",
                "2021",
                "2020",
                "2021",
                "2021",
                "2020",
                "2021",
                "2020",
                "2021",
                "2021",
                "2021",
                "2020",
                "2021"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555004",
            "country": "Japan",
            "country_code": "JPN",
            "group_name": "TA551",
            "incidents_sent": 4,
            "latitude": "36.0000",
            "longitude": "138.0000",
            "year_list": [
                "2021",
                "2020",
                "2020",
                "2021"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555005",
            "country": "Hong Kong",
            "country_code": "HKG",
            "group_name": "TropicTrooper",
            "incidents_sent": 10,
            "latitude": "22.2500",
            "longitude": "114.1667",
            "year_list": [
                "2020",
                "2016",
                "2017",
                "2015",
                "2016",
                "2021",
                "2020",
                "2018",
                "2020",
                "2018"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555006",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "Turla",
            "incidents_sent": 24,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2015",
                "2017",
                "2019",
                "2017",
                "2020",
                "2017",
                "2019",
                "2018",
                "2020",
                "2018",
                "2020",
                "2021",
                "2019",
                "2020",
                "2014",
                "2017",
                "2019",
                "2020",
                "2013",
                "2020",
                "2020",
                "2018",
                "2016",
                "2018"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555007",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "Windigo",
            "incidents_sent": 4,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2014",
                "2019",
                "2017",
                "2018"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555008",
            "country": "China",
            "country_code": "CHN",
            "group_name": "ZIRCONIUM",
            "incidents_sent": 4,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2020",
                "2021",
                "2020",
                "2020"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555009",
            "country": "China",
            "country_code": "CHN",
            "group_name": "APT 3, Gothic Panda, Buckeye",
            "incidents_sent": 8,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2014",
                "2015",
                "2007",
                "2014",
                "2016",
                "2016",
                "2016",
                "2014"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055500a",
            "country": "Iran",
            "country_code": "IRN",
            "group_name": "APT 33, Elfin, Magnallium",
            "incidents_sent": 3,
            "latitude": "32.0000",
            "longitude": "53.0000",
            "year_list": [
                "2019",
                "2019",
                "2019"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055500b",
            "country": "South Asia",
            "country_code": "SAS",
            "group_name": "Bitter",
            "incidents_sent": 5,
            "latitude": "20.0000",
            "longitude": "77.0000",
            "year_list": [
                "2013",
                "2016",
                "2018",
                "2019",
                "2020"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055500c",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "Buhtrap, Ratopak Spider",
            "incidents_sent": 6,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2015",
                "2014",
                "2016",
                "2019",
                "2015",
                "2017"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055500d",
            "country": "USA",
            "country_code": "USA",
            "group_name": "Subgroup: [Unnamed group USA]",
            "incidents_sent": 2,
            "latitude": "38.0000",
            "longitude": "-97.0000",
            "year_list": [
                "2020",
                "2019"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055500e",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "RTM",
            "incidents_sent": 3,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2017",
                "2019",
                "2019"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055500f",
            "country": "China",
            "country_code": "CHN",
            "group_name": "APT 4, Maverick Panda, Wisp Team",
            "incidents_sent": 7,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2012",
                "2011",
                "2015",
                "2012",
                "2018",
                "2013",
                "2013"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555010",
            "country": "USA",
            "country_code": "USA",
            "group_name": "CIA",
            "incidents_sent": 2,
            "latitude": "38.0000",
            "longitude": "-97.0000",
            "year_list": [
                "2018",
                "2018"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555011",
            "country": "China",
            "country_code": "CHN",
            "group_name": "PittyTiger",
            "incidents_sent": 2,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2014",
                "2014"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555012",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Rocke",
            "incidents_sent": 3,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2019",
                "2019",
                "2018"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555013",
            "country": "China",
            "country_code": "CHN",
            "group_name": "ScarletMimic",
            "incidents_sent": 1,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2016"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555014",
            "country": "Azerbaijan",
            "country_code": "AZE",
            "group_name": "Silence",
            "incidents_sent": 5,
            "latitude": "40.5000",
            "longitude": "47.5000",
            "year_list": [
                "2018",
                "2019",
                "2019",
                "2020",
                "2017"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555015",
            "country": "Niger",
            "country_code": "NER",
            "group_name": "SilverTerrier",
            "incidents_sent": 2,
            "latitude": "16.0000",
            "longitude": "8.0000",
            "year_list": [
                "2016",
                "2016"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555016",
            "country": "China",
            "country_code": "CHN",
            "group_name": "WinntiGroup",
            "incidents_sent": 6,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2015",
                "2018",
                "2020",
                "2015",
                "2016",
                "2013"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555017",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "WizardSpider",
            "incidents_sent": 13,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2020",
                "2019",
                "2019",
                "2019",
                "2019",
                "2020",
                "2020",
                "2017",
                "2020",
                "2020",
                "2020",
                "2020",
                "2019"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555018",
            "country": "Middle East",
            "country_code": "MEA",
            "group_name": "BlackOasis",
            "incidents_sent": 3,
            "latitude": "35.8333",
            "longitude": "14.5833",
            "year_list": [
                "2017",
                "2017",
                "2015"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555019",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "TA505",
            "incidents_sent": 11,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2019",
                "2019",
                "2019",
                "2017",
                "2019",
                "2019",
                "2019",
                "2020",
                "2018",
                "2018",
                "2018"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055501a",
            "country": "Belarus",
            "country_code": "BLR",
            "group_name": "TA459",
            "incidents_sent": 1,
            "latitude": "53.0000",
            "longitude": "28.0000",
            "year_list": [
                "2017"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055501b",
            "country": "China",
            "country_code": "CHN",
            "group_name": "OperationWocao",
            "incidents_sent": 1,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2019"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055501c",
            "country": "United States",
            "country_code": "USA",
            "group_name": "Orangeworm",
            "incidents_sent": 1,
            "latitude": "38.0000",
            "longitude": "-97.0000",
            "year_list": [
                "2018"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055501d",
            "country": "Lebanon",
            "country_code": "LBN",
            "group_name": "VolatileCedar",
            "incidents_sent": 2,
            "latitude": "33.8333",
            "longitude": "35.8333",
            "year_list": [
                "2015",
                "2021"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055501e",
            "country": "China",
            "country_code": "CHN",
            "group_name": "APT 18, Dynamite Panda, Wekby",
            "incidents_sent": 5,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2015",
                "2016",
                "2014",
                "2014",
                "2015"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055501f",
            "country": "China",
            "country_code": "CHN",
            "group_name": "PLATINUM",
            "incidents_sent": 3,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2016",
                "2017",
                "2018"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555020",
            "country": "North Korea",
            "country_code": "PRK",
            "group_name": "StolenPencil",
            "incidents_sent": 1,
            "latitude": "37.0000",
            "longitude": "127.5000",
            "year_list": [
                "2018"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555021",
            "country": "Singapore",
            "country_code": "SGP",
            "group_name": "Whitefly",
            "incidents_sent": 1,
            "latitude": "1.3667",
            "longitude": "103.8000",
            "year_list": [
                "2019"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555022",
            "country": "Iran",
            "country_code": "IRN",
            "group_name": "Chafer, APT 39",
            "incidents_sent": 4,
            "latitude": "32.0000",
            "longitude": "53.0000",
            "year_list": [
                "2018",
                "2017",
                "2018",
                "2018"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555023",
            "country": "China",
            "country_code": "CHN",
            "group_name": "APT 31, Judgment Panda, Zirconium",
            "incidents_sent": 2,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2020",
                "2020"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555024",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Blackgear",
            "incidents_sent": 1,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2018"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555025",
            "country": "China",
            "country_code": "CHN",
            "group_name": "APT 20, Violin Panda",
            "incidents_sent": 1,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2017"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555026",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Axiom, Group 72",
            "incidents_sent": 1,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2008/2014"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555027",
            "country": "China",
            "country_code": "CHN",
            "group_name": "PutterPanda",
            "incidents_sent": 2,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2016",
                "2014"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555028",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Suckfly",
            "incidents_sent": 4,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2016",
                "2016",
                "2015",
                "2014"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555029",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Rancor",
            "incidents_sent": 1,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2018"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055502a",
            "country": "United Arab Emirates",
            "country_code": "ARE",
            "group_name": "StealthFalcon",
            "incidents_sent": 1,
            "latitude": "24.0000",
            "longitude": "54.0000",
            "year_list": [
                "2016"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055502b",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Taidoor",
            "incidents_sent": 1,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2012"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055502c",
            "country": "Brazil",
            "country_code": "BRA",
            "group_name": "PoseidonGroup",
            "incidents_sent": 1,
            "latitude": "-10.0000",
            "longitude": "-55.0000",
            "year_list": [
                "2016"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055502d",
            "country": "Pakistan",
            "country_code": "PAK",
            "group_name": "TheWhiteCompany",
            "incidents_sent": 1,
            "latitude": "30.0000",
            "longitude": "70.0000",
            "year_list": [
                "2018"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055502e",
            "country": "China",
            "country_code": "CHN",
            "group_name": "APT 5, Keyhole Panda",
            "incidents_sent": 1,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2019"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055502f",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Calypso",
            "incidents_sent": 1,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2021"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555030",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "Cyber Berkut",
            "incidents_sent": 4,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2015",
                "2014",
                "2014",
                "2015"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555031",
            "country": "ISIS",
            "country_code": "SYR",
            "group_name": "Cyber Caliphate Army (CCA), United Cyber Caliphate (UCC)",
            "incidents_sent": 10,
            "latitude": "35.0000",
            "longitude": "38.0000",
            "year_list": [
                "2015",
                "2015",
                "2015",
                "2015",
                "2017",
                "2015",
                "2015",
                "2015",
                "2015",
                "2015"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555032",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "Doppel Spider",
            "incidents_sent": 11,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2021",
                "2020",
                "2021",
                "2020",
                "2020",
                "2020",
                "2020",
                "2020",
                "2020",
                "2020",
                "2020"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555033",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Emissary Panda, APT 27, LuckyMouse, Bronze Union",
            "incidents_sent": 14,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2020",
                "2020",
                "2020",
                "2020",
                "2015",
                "2020",
                "2021",
                "2010",
                "2018",
                "2017",
                "2019",
                "2020",
                "2018",
                "2019"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555034",
            "country": "Iran",
            "country_code": "IRN",
            "group_name": "Flying Kitten, Ajax Security Team",
            "incidents_sent": 1,
            "latitude": "32.0000",
            "longitude": "53.0000",
            "year_list": [
                "2013"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555035",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "Gamaredon Group",
            "incidents_sent": 9,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2019",
                "2019",
                "2021",
                "2020",
                "2019",
                "2019",
                "2019",
                "2019",
                "2020"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555036",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Goblin Panda, Cycldek, Conimes",
            "incidents_sent": 4,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2017",
                "2020",
                "2018",
                "2016"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555037",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Hurricane Panda",
            "incidents_sent": 1,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2014"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555038",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Icefog, Dagger Panda",
            "incidents_sent": 2,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2014",
                "2018"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555039",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "InvisiMole",
            "incidents_sent": 1,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2019"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055503a",
            "country": "North Korea",
            "country_code": "PRK",
            "group_name": "Kimsuky, Velvet Chollima",
            "incidents_sent": 17,
            "latitude": "37.0000",
            "longitude": "127.5000",
            "year_list": [
                "2018",
                "2018",
                "2019",
                "2019",
                "2018",
                "2019",
                "2020",
                "2019",
                "2020",
                "2013",
                "2018",
                "2020",
                "2014",
                "2019",
                "2018",
                "2020",
                "2020"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055503b",
            "country": "North Korea",
            "country_code": "PRK",
            "group_name": "Lazarus Group, Hidden Cobra, Labyrinth Chollima",
            "incidents_sent": 54,
            "latitude": "37.0000",
            "longitude": "127.5000",
            "year_list": [
                "2021",
                "2021",
                "2011",
                "2019",
                "2020",
                "2020",
                "2019",
                "2017",
                "2018",
                "2018",
                "2013",
                "2017",
                "2018",
                "2020",
                "2021",
                "2013",
                "2017",
                "2020",
                "2020",
                "2018",
                "2009",
                "2019",
                "2019",
                "2020",
                "2017",
                "2019",
                "2019",
                "2020",
                "2020",
                "2020",
                "2013",
                "2017",
                "2020",
                "2020",
                "2014",
                "2017",
                "2018",
                "2018",
                "2020",
                "2014",
                "2017",
                "2018",
                "2020",
                "2015",
                "2021",
                "2018",
                "2018",
                "2019",
                "2020",
                "2017",
                "2019",
                "2018",
                "2019",
                "2021"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055503c",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "Cobalt Group",
            "incidents_sent": 11,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2017",
                "2017",
                "2018",
                "2016",
                "2018",
                "2017",
                "2016",
                "2016",
                "2019",
                "2018",
                "2018"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055503d",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "Energetic Bear, Dragonfly",
            "incidents_sent": 11,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2015",
                "2016",
                "2017",
                "2013",
                "2020",
                "2016",
                "2020",
                "2016",
                "2017",
                "2014",
                "2016"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055503e",
            "country": "UK",
            "country_code": "GBR",
            "group_name": "GCHQ",
            "incidents_sent": 2,
            "latitude": "54.0000",
            "longitude": "-2.0000",
            "year_list": [
                "2010",
                "2009"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055503f",
            "country": "Pakistan",
            "country_code": "PAK",
            "group_name": "Gorgon Group",
            "incidents_sent": 4,
            "latitude": "30.0000",
            "longitude": "70.0000",
            "year_list": [
                "2018",
                "2017",
                "2020",
                "2020"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555040",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "Inception Framework, Cloud Atlas",
            "incidents_sent": 5,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2019",
                "2012",
                "2018",
                "2014",
                "2014"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555041",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "Indrik Spider",
            "incidents_sent": 13,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2020",
                "2021",
                "2019",
                "2021",
                "2021",
                "2020",
                "2019",
                "2019",
                "2019",
                "2020",
                "2018",
                "2017",
                "2019"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555042",
            "country": "North Korea",
            "country_code": "PRK",
            "group_name": "Subgroup: Bluenoroff, APT 38, Stardust Chollima",
            "incidents_sent": 11,
            "latitude": "37.0000",
            "longitude": "127.5000",
            "year_list": [
                "2018",
                "2018",
                "2015",
                "2016",
                "2018",
                "2015",
                "2015",
                "2017",
                "2017",
                "2018",
                "2016"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555043",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Leviathan, APT 40, TEMP.Periscope",
            "incidents_sent": 5,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2017",
                "2018",
                "2014",
                "2017",
                "2020"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555044",
            "country": "Iran",
            "country_code": "IRN",
            "group_name": "CopyKittens, Slayer Kitten",
            "incidents_sent": 3,
            "latitude": "32.0000",
            "longitude": "53.0000",
            "year_list": [
                "2013",
                "2015",
                "2017"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555045",
            "country": "Iran",
            "country_code": "IRN",
            "group_name": "Cutting Kitten, TG-2889",
            "incidents_sent": 3,
            "latitude": "32.0000",
            "longitude": "53.0000",
            "year_list": [
                "2013",
                "2012",
                "2015"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555046",
            "country": "Lebanon",
            "country_code": "LBN",
            "group_name": "Dark Caracal",
            "incidents_sent": 2,
            "latitude": "33.8333",
            "longitude": "35.8333",
            "year_list": [
                "2012",
                "2020"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555047",
            "country": "South Korea",
            "country_code": "KOR",
            "group_name": "DarkHotel",
            "incidents_sent": 15,
            "latitude": "37.0000",
            "longitude": "127.5000",
            "year_list": [
                "2020",
                "2018",
                "2020",
                "2020",
                "2020",
                "2020",
                "2010",
                "2020",
                "2018",
                "2020",
                "2016",
                "2015",
                "2010",
                "2015",
                "2020"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555048",
            "country": "Gaza",
            "country_code": "GZS",
            "group_name": "Desert Falcons",
            "incidents_sent": 11,
            "latitude": "32.0000",
            "longitude": "35.2500",
            "year_list": [
                "2017",
                "2018",
                "2015",
                "2015",
                "2016",
                "2017",
                "2015",
                "2017",
                "2020",
                "2020",
                "2017"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555049",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Ke3chang, Vixen Panda, APT 15, GREF, Playful Dragon",
            "incidents_sent": 8,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2010",
                "2017",
                "2020",
                "2014",
                "2019",
                "2015",
                "2016",
                "2018"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055504a",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Comment Crew, APT 1",
            "incidents_sent": 7,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2011",
                "2014",
                "2018",
                "2018",
                "2011",
                "2011",
                "2014"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055504b",
            "country": "India",
            "country_code": "IND",
            "group_name": "Confucius",
            "incidents_sent": 3,
            "latitude": "20.0000",
            "longitude": "77.0000",
            "year_list": [
                "2018",
                "2017",
                "2017"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055504c",
            "country": "Iran",
            "country_code": "IRN",
            "group_name": "DarkHydrus, LazyMeerkat",
            "incidents_sent": 4,
            "latitude": "32.0000",
            "longitude": "53.0000",
            "year_list": [
                "2018",
                "2019",
                "2018",
                "2019"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055504d",
            "country": "Iran",
            "country_code": "IRN",
            "group_name": "Domestic Kitten",
            "incidents_sent": 1,
            "latitude": "32.0000",
            "longitude": "53.0000",
            "year_list": [
                "2020"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055504e",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Evil Eye",
            "incidents_sent": 3,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2018",
                "2020",
                "2020"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055504f",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Gelsemium",
            "incidents_sent": 2,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2014",
                "2021"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555050",
            "country": "Iran",
            "country_code": "IRN",
            "group_name": "Iridium",
            "incidents_sent": 3,
            "latitude": "32.0000",
            "longitude": "53.0000",
            "year_list": [
                "2018",
                "2018",
                "2018"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555051",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "Hades",
            "incidents_sent": 3,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2019",
                "2020",
                "2020"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555052",
            "country": "Iran",
            "country_code": "IRN",
            "group_name": "ITG18",
            "incidents_sent": 1,
            "latitude": "32.0000",
            "longitude": "53.0000",
            "year_list": [
                "2020"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555053",
            "country": "North Korea",
            "country_code": "PRK",
            "group_name": "Subgroup: BeagleBoyz",
            "incidents_sent": 2,
            "latitude": "37.0000",
            "longitude": "127.5000",
            "year_list": [
                "2016",
                "2016"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555054",
            "country": "Iran",
            "country_code": "IRN",
            "group_name": "DNSpionage",
            "incidents_sent": 1,
            "latitude": "32.0000",
            "longitude": "53.0000",
            "year_list": [
                "2019"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555055",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Hidden Lynx, Aurora Panda",
            "incidents_sent": 2,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2012",
                "2012"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555056",
            "country": "North Korea",
            "country_code": "PRK",
            "group_name": "Subgroup: Andariel, Silent Chollima",
            "incidents_sent": 3,
            "latitude": "37.0000",
            "longitude": "127.5000",
            "year_list": [
                "2021",
                "2021",
                "2018"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555057",
            "country": "Iran",
            "country_code": "IRN",
            "group_name": "Infy, Prince of Persia",
            "incidents_sent": 2,
            "latitude": "32.0000",
            "longitude": "53.0000",
            "year_list": [
                "2015",
                "2017"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555058",
            "country": "Iran",
            "country_code": "IRN",
            "group_name": "Magic Hound, APT 35, Cobalt Gypsy, Charming Kitten",
            "incidents_sent": 15,
            "latitude": "32.0000",
            "longitude": "53.0000",
            "year_list": [
                "2019",
                "2020",
                "Mid-2014",
                "2017",
                "2016",
                "2019",
                "2020",
                "2020",
                "2018",
                "2018",
                "2020",
                "2019",
                "2017",
                "2020",
                "2017"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555059",
            "country": "Gaza",
            "country_code": "GZS",
            "group_name": "Molerats, Extreme Jackal, Gaza Cybergang",
            "incidents_sent": 24,
            "latitude": "32.0000",
            "longitude": "35.2500",
            "year_list": [
                "2014",
                "2021",
                "2014",
                "2016",
                "2015",
                "2017",
                "2015",
                "2015",
                "2020",
                "2019",
                "2020",
                "2013",
                "2016",
                "2020",
                "2012",
                "2014",
                "2019",
                "2019",
                "2016",
                "2012",
                "2017",
                "2019",
                "2019",
                "2020"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055505a",
            "country": "Iran",
            "country_code": "IRN",
            "group_name": "MuddyWater, Seedworm, TEMP.Zagros, Static Kitten",
            "incidents_sent": 18,
            "latitude": "32.0000",
            "longitude": "53.0000",
            "year_list": [
                "2020",
                "2021",
                "2018",
                "2018",
                "2018",
                "2018",
                "2021",
                "2018",
                "2020",
                "2018",
                "2019",
                "2017",
                "2019",
                "2019",
                "2019",
                "2019",
                "2019",
                "2020"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055505b",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Mustang Panda, Bronze President",
            "incidents_sent": 5,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2019",
                "2014",
                "2020",
                "2020",
                "2020"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055505c",
            "country": "Iran",
            "country_code": "IRN",
            "group_name": "OilRig, APT 34, Helix Kitten, Chrysene",
            "incidents_sent": 24,
            "latitude": "32.0000",
            "longitude": "53.0000",
            "year_list": [
                "2017",
                "2018",
                "2016",
                "2017",
                "2020",
                "2016",
                "2012",
                "2016",
                "2021",
                "2018",
                "2019",
                "2017",
                "2016",
                "2016",
                "2018",
                "2019",
                "2016",
                "2020",
                "2016",
                "2017",
                "2017",
                "2018",
                "2018",
                "2020"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055505d",
            "country": "Iran",
            "country_code": "IRN",
            "group_name": "Subgroup: Greenbug, Volatile Kitten",
            "incidents_sent": 4,
            "latitude": "32.0000",
            "longitude": "53.0000",
            "year_list": [
                "2017",
                "2017",
                "2016",
                "2017"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055505e",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Operation DRBControl",
            "incidents_sent": 14,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2020",
                "2010",
                "2021",
                "2015",
                "2018",
                "2019",
                "2020",
                "2020",
                "2019",
                "2020",
                "2017",
                "2018",
                "2020",
                "2020"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055505f",
            "country": "Iran",
            "country_code": "IRN",
            "group_name": "Parisite, Fox Kitten, Pioneer Kitten",
            "incidents_sent": 3,
            "latitude": "32.0000",
            "longitude": "53.0000",
            "year_list": [
                "2020",
                "2019",
                "2020"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555060",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "Pinchy Spider, Gold Southfield",
            "incidents_sent": 42,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2019",
                "2020",
                "2020",
                "2021",
                "2021",
                "2019",
                "2020",
                "2020",
                "2020",
                "2020",
                "2020",
                "2020",
                "2020",
                "2020",
                "2021",
                "2020",
                "2020",
                "2021",
                "2021",
                "2021",
                "2021",
                "2020",
                "2019",
                "2019",
                "2020",
                "2020",
                "2021",
                "2020",
                "2019",
                "2020",
                "2020",
                "2021",
                "2020",
                "2021",
                "2021",
                "2020",
                "2020",
                "2021",
                "2020",
                "2020",
                "2019",
                "2021"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555061",
            "country": "North Korea",
            "country_code": "PRK",
            "group_name": "Reaper, APT 37, Ricochet Chollima, ScarCruft",
            "incidents_sent": 21,
            "latitude": "37.0000",
            "longitude": "127.5000",
            "year_list": [
                "2018",
                "2020",
                "2016",
                "2020",
                "2018",
                "2019",
                "2017",
                "2019",
                "2016",
                "2019",
                "2020",
                "2019",
                "2019",
                "2020",
                "2019",
                "2018",
                "2016",
                "2017",
                "2018",
                "2018",
                "2019"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555062",
            "country": "Iran",
            "country_code": "IRN",
            "group_name": "Rocket Kitten, Newscaster, NewsBeef",
            "incidents_sent": 4,
            "latitude": "32.0000",
            "longitude": "53.0000",
            "year_list": [
                "2017",
                "2011",
                "2016",
                "2015"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555063",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "Sofacy, APT 28, Fancy Bear, Sednit",
            "incidents_sent": 57,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2015",
                "2015",
                "2018",
                "2019",
                "2015",
                "2019",
                "2015",
                "2017",
                "2018",
                "2018",
                "2015",
                "2016",
                "2017",
                "2015",
                "2016",
                "2017",
                "2018",
                "2018",
                "2019",
                "2014",
                "2015",
                "2016",
                "2017",
                "2016",
                "2017",
                "2019",
                "2019",
                "2019",
                "2020",
                "2014",
                "2016",
                "2016",
                "2020",
                "2016",
                "2019",
                "2016",
                "2017",
                "2018",
                "2018",
                "2015",
                "2015",
                "2018",
                "2018",
                "2015",
                "2015",
                "2017",
                "2015",
                "2016",
                "2016",
                "2016",
                "2016",
                "2019",
                "2021",
                "2017",
                "2018",
                "2020",
                "2020"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555064",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Lotus Blossom, Spring Dragon, Thrip",
            "incidents_sent": 7,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2018",
                "2018",
                "2015",
                "2018",
                "2018",
                "2015",
                "2017"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555065",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Naikon, Lotus Panda",
            "incidents_sent": 5,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2013",
                "2015",
                "2013",
                "2017",
                "2014"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555066",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Poison Carp, Evil Eye",
            "incidents_sent": 3,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2018",
                "2020",
                "2020"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555067",
            "country": "Turkey",
            "country_code": "TUR",
            "group_name": "Promethium, StrongPity",
            "incidents_sent": 5,
            "latitude": "39.0000",
            "longitude": "35.0000",
            "year_list": [
                "2018",
                "2019",
                "2019",
                "2020",
                "2018"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555068",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "Sandworm Team, Iron Viking, Voodoo Bear",
            "incidents_sent": 4,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2017",
                "2015",
                "2019",
                "2014"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555069",
            "country": "China",
            "country_code": "CHN",
            "group_name": "RedDelta",
            "incidents_sent": 3,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2020",
                "2020",
                "2021"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055506a",
            "country": "Iran",
            "country_code": "IRN",
            "group_name": "Mabna Institute, Cobalt Dickens, Silent Librarian",
            "incidents_sent": 3,
            "latitude": "32.0000",
            "longitude": "53.0000",
            "year_list": [
                "2020",
                "2018",
                "2019"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055506b",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Platinum",
            "incidents_sent": 4,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2017",
                "2017",
                "2017",
                "2019"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055506c",
            "country": "China",
            "country_code": "CHN",
            "group_name": "NetTraveler, APT 21, Hammer Panda",
            "incidents_sent": 2,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2015",
                "2014"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055506d",
            "country": "India",
            "country_code": "IND",
            "group_name": "Patchwork, Dropping Elephant",
            "incidents_sent": 3,
            "latitude": "20.0000",
            "longitude": "77.0000",
            "year_list": [
                "2018",
                "2015",
                "2018"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055506e",
            "country": "China",
            "country_code": "CHN",
            "group_name": "PittyTiger, Pitty Panda",
            "incidents_sent": 4,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2011",
                "2014",
                "2014",
                "2014"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055506f",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Nightshade Panda, APT 9, Group 27",
            "incidents_sent": 5,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2015",
                "2015",
                "2016",
                "2015",
                "2015"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555070",
            "country": "China",
            "country_code": "CHN",
            "group_name": "RedAlpha",
            "incidents_sent": 2,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2017",
                "2017"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555071",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Mikroceen",
            "incidents_sent": 1,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2021"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555072",
            "country": "India",
            "country_code": "IND",
            "group_name": "Operation HangOver, Monsoon, Viceroy Tiger",
            "incidents_sent": 1,
            "latitude": "20.0000",
            "longitude": "77.0000",
            "year_list": [
                "2020"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555073",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Nitro, Covert Grove",
            "incidents_sent": 1,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2014"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555074",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "Operation Ghostwriter",
            "incidents_sent": 2,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2021",
                "2021"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555075",
            "country": "Turkey",
            "country_code": "TUR",
            "group_name": "Sea Turtle",
            "incidents_sent": 1,
            "latitude": "39.0000",
            "longitude": "35.0000",
            "year_list": [
                "2019"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555076",
            "country": "Iran",
            "country_code": "IRN",
            "group_name": "Madi",
            "incidents_sent": 1,
            "latitude": "32.0000",
            "longitude": "53.0000",
            "year_list": [
                "2012"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555077",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "Operation Domino, Operation Kremlin",
            "incidents_sent": 2,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2020",
                "2020"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555078",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Roaming Tiger",
            "incidents_sent": 1,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2015"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555079",
            "country": "India",
            "country_code": "IND",
            "group_name": "SideWinder, Rattlesnake",
            "incidents_sent": 1,
            "latitude": "20.0000",
            "longitude": "77.0000",
            "year_list": [
                "2019"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055507a",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Stone Panda, APT 10, menuPass",
            "incidents_sent": 18,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2019",
                "2021",
                "2016",
                "2017",
                "2018",
                "2017",
                "2016",
                "2019",
                "2016",
                "2018",
                "2019",
                "2019",
                "2019",
                "2017",
                "2016",
                "2018",
                "2016",
                "2017"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055507b",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "TA505, Graceful Spider, Gold Evergreen",
            "incidents_sent": 20,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2018",
                "2019",
                "2020",
                "2020",
                "2018",
                "2019",
                "2019",
                "2019",
                "2020",
                "2018",
                "2019",
                "2017",
                "2020",
                "2019",
                "2019",
                "2019",
                "2019",
                "2018",
                "2019",
                "2019"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055507c",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "Turla, Waterbug, Venomous Bear",
            "incidents_sent": 31,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2019",
                "2020",
                "2015",
                "2017",
                "2017",
                "2018",
                "2015",
                "2016",
                "2017",
                "2014",
                "2017",
                "2014",
                "2015",
                "2019",
                "2008",
                "2017",
                "2017",
                "2018",
                "2019",
                "2018",
                "2019",
                "2017",
                "2013",
                "2016",
                "2018",
                "2019",
                "2019",
                "2021",
                "1996",
                "2020",
                "2020"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055507d",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Winnti Group, Blackfly, Wicked Panda",
            "incidents_sent": 20,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2019",
                "2015",
                "2011",
                "2011",
                "2015",
                "2015",
                "2016",
                "2018",
                "2019",
                "2016",
                "2020",
                "2014",
                "2019",
                "2015",
                "2014",
                "2019",
                "2021",
                "2016",
                "2017",
                "2018"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055507e",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "Wizard Spider, Gold Blackburn",
            "incidents_sent": 50,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2020",
                "2020",
                "2021",
                "2021",
                "2020",
                "2021",
                "2021",
                "2019",
                "2020",
                "2021",
                "2019",
                "2020",
                "2020",
                "2020",
                "2019",
                "2019",
                "2020",
                "2020",
                "2021",
                "2021",
                "2021",
                "2019",
                "2020",
                "2020",
                "2020",
                "2021",
                "2019",
                "2020",
                "2019",
                "2019",
                "2020",
                "2020",
                "2020",
                "2019",
                "2019",
                "2020",
                "2020",
                "2020",
                "2021",
                "2020",
                "2020",
                "2020",
                "2020",
                "2020",
                "2019",
                "2020",
                "2021",
                "2021",
                "2019",
                "2020"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055507f",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "Guru Spider",
            "incidents_sent": 3,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2016",
                "2018",
                "2018"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555080",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Rocke, Iron Group",
            "incidents_sent": 9,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2018",
                "2019",
                "2018",
                "2021",
                "2021",
                "2019",
                "2019",
                "2019",
                "2019"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555081",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Yingmob",
            "incidents_sent": 1,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2017"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555082",
            "country": "Pakistan",
            "country_code": "PAK",
            "group_name": "Transparent Tribe, APT 36",
            "incidents_sent": 13,
            "latitude": "30.0000",
            "longitude": "70.0000",
            "year_list": [
                "2019",
                "2020",
                "2019",
                "2020",
                "2020",
                "2021",
                "2016",
                "2012",
                "2019",
                "2020",
                "2016",
                "2016",
                "2017"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555083",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Tropic Trooper, Pirate Panda, APT 23, KeyBoy",
            "incidents_sent": 11,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2016",
                "2020",
                "2012",
                "2015",
                "2014",
                "2016",
                "2014",
                "2017",
                "2020",
                "2013",
                "2017"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555084",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "UNC2452, Dark Halo, SolarStorm",
            "incidents_sent": 15,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2020",
                "2016",
                "2013",
                "2015",
                "2019",
                "2014",
                "2016",
                "2013",
                "2016",
                "2017",
                "2018",
                "2021",
                "2017",
                "2013",
                "2017"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555085",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Vicious Panda",
            "incidents_sent": 3,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2017",
                "2020",
                "2015"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555086",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "Avalanche",
            "incidents_sent": 1,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2010"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555087",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "Cron",
            "incidents_sent": 1,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2017"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555088",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "Dungeon Spider",
            "incidents_sent": 12,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2016",
                "2018",
                "2017",
                "2017",
                "2016",
                "2017",
                "2017",
                "2016",
                "2016",
                "2017",
                "2017",
                "2016"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555089",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "Monty Spider",
            "incidents_sent": 11,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2019",
                "2018",
                "2017",
                "2017",
                "2018",
                "2020",
                "2016",
                "2017",
                "2018",
                "2017",
                "2018"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055508a",
            "country": "Saudi Arabia",
            "country_code": "SAU",
            "group_name": "OurMine",
            "incidents_sent": 13,
            "latitude": "25.0000",
            "longitude": "45.0000",
            "year_list": [
                "2016",
                "2017",
                "2016",
                "2017",
                "2020",
                "2017",
                "2017",
                "2017",
                "2017",
                "2017",
                "2020",
                "2016",
                "2020"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055508b",
            "country": "UAE",
            "country_code": "ARE",
            "group_name": "Stealth Falcon, FruityArmor",
            "incidents_sent": 5,
            "latitude": "24.0000",
            "longitude": "54.0000",
            "year_list": [
                "2019",
                "2018",
                "2016",
                "2014",
                "2018"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055508c",
            "country": "China",
            "country_code": "CHN",
            "group_name": "TA428",
            "incidents_sent": 5,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2020",
                "2019",
                "2019",
                "2020",
                "2020"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055508d",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "TeleBots",
            "incidents_sent": 7,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2016",
                "2017",
                "2017",
                "2017",
                "2017",
                "2017",
                "2017"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055508e",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "Salty Spider",
            "incidents_sent": 2,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2014",
                "2018"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055508f",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Tonto Team, HartBeat, Karma Panda",
            "incidents_sent": 6,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2019",
                "2019",
                "2017",
                "2019",
                "2021",
                "2009"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555090",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Turbine Panda, APT 26, Shell Crew, WebMasters, KungFu Kittens",
            "incidents_sent": 3,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2012",
                "2015",
                "2012"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555091",
            "country": "Lebanon",
            "country_code": "LBN",
            "group_name": "Volatile Cedar",
            "incidents_sent": 2,
            "latitude": "33.8333",
            "longitude": "35.8333",
            "year_list": [
                "2015",
                "2020"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555092",
            "country": "Kazakhstan",
            "country_code": "KAZ",
            "group_name": "Fxmsp",
            "incidents_sent": 1,
            "latitude": "48.0000",
            "longitude": "68.0000",
            "year_list": [
                "2019"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555093",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "Shark Spider",
            "incidents_sent": 1,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2013"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555094",
            "country": "USA",
            "country_code": "USA",
            "group_name": "Shadow Brokers",
            "incidents_sent": 9,
            "latitude": "38.0000",
            "longitude": "-97.0000",
            "year_list": [
                "2017",
                "2016",
                "2017",
                "2016",
                "2017",
                "2016",
                "2017",
                "2017",
                "2017"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555095",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "Zombie Spider",
            "incidents_sent": 1,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2017"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555096",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "TeamSpy Crew",
            "incidents_sent": 1,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2017"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555097",
            "country": "Pakistan",
            "country_code": "PAK",
            "group_name": "Gnosticplayers",
            "incidents_sent": 7,
            "latitude": "30.0000",
            "longitude": "70.0000",
            "year_list": [
                "2019",
                "2019",
                "2019",
                "2019",
                "2019",
                "2019",
                "2019"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555098",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Yanbian Gang",
            "incidents_sent": 1,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2020"
            ]
        },
        {
            "_id": "613b25bb4ee0156be0555099",
            "country": "China",
            "country_code": "CHN",
            "group_name": "TA413",
            "incidents_sent": 1,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2021"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055509a",
            "country": "Iran",
            "country_code": "IRN",
            "group_name": "Tortoiseshell, Imperial Kitten",
            "incidents_sent": 1,
            "latitude": "32.0000",
            "longitude": "53.0000",
            "year_list": [
                "2019"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055509b",
            "country": "Russia",
            "country_code": "RUS",
            "group_name": "Venom Spider, Golden Chickens",
            "incidents_sent": 1,
            "latitude": "60.0000",
            "longitude": "100.0000",
            "year_list": [
                "2019"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055509c",
            "country": "China",
            "country_code": "CHN",
            "group_name": "Pacha Group",
            "incidents_sent": 2,
            "latitude": "35.0000",
            "longitude": "105.0000",
            "year_list": [
                "2018",
                "2019"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055509d",
            "country": "Syria",
            "country_code": "SYR",
            "group_name": "Syrian Electronic Army (SEA), Deadeye Jackal",
            "incidents_sent": 2,
            "latitude": "35.0000",
            "longitude": "38.0000",
            "year_list": [
                "2016",
                "2018"
            ]
        },
        {
            "_id": "613b25bb4ee0156be055509e",
            "country": "North Korea",
            "country_code": "PRK",
            "group_name": "Wassonite",
            "incidents_sent": 1,
            "latitude": "37.0000",
            "longitude": "127.5000",
            "year_list": [
                "2019"
            ]
        }
    ])

    const Table = Tables[collection]
    
    const getcollection = async (collection) => {
        if (!collection)
            return
        const doc_list = await fetch(`${API}/rawdata/${collection}`, {
            method: 'GET',
        })
        const doc_list_data = await doc_list.json();
        setTable(doc_list_data)
    }

    const renderTable = (collection) => {
        if (!collection) 
            return
        getcollection(collection)
    }

    return (
        <div>
            <h2 className='page-header'>{collection}</h2>
            <div className="row">
                <div className="col-6">
                    <div className="card">
                        <div className="card__body">
                            <label>Select Collection</label>
                            <select name="" id="" onChange={(e) => {setCollection(e.target.value); console.log(e.target.value); renderTable(e.target.value)}}>
                                <option value="APT_Total_incident_by_group">APT_Total_incident_by_group</option>
                                <option value="APT_Total_incident_received_by_country_table">APT_Total_incident_received_by_country_table</option>
                                <option value="APT_Total_incident_sent_by_country_table">APT_Total_incident_sent_by_country_table</option>
                                <option value="APT_Total_incidents_sent_by_years_table">APT_Total_incidents_sent_by_years_table</option>
                                <option value="APT_Total_incidents_by_country_pairs_years_table">APT_Total_incidents_by_country_pairs_years_table</option>
                                <option value="APT_Total_incidents_by_country_pairs_table">APT_Total_incidents_by_country_pairs_table</option>
                                <option value="APT_GEO_Context_2021_missing">APT_GEO_Context_2021_missing</option>
                                <option value="APT_GEO_Context_complete">APT_GEO_Context_complete</option>
                                <option value="APT_Group_Incidents">APT_Group_Incidents</option>
                                <option value="APT_Group_Incidents_CAMEO">APT_Group_Incidents_CAMEO</option>
                            </select>
                        </div>
                    </div>
                </div>
            </div>
            <div className="row">
                <div className="col-12">
                    <div className="card">
                        <div className="card__body">
                            {<Table
                                headData = {default_table_head}
                                renderHead={(item, index) => renderHead(item, index)}
                                bodyData={table_data}
                                renderBody={(item, index) => renderBody(item, index)}
                            />}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Rawdata

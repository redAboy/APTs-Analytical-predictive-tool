import React from 'react'

import { Link } from 'react-router-dom'

import Chart from 'react-apexcharts'

import StatusCard from '../components/status-card/StatusCard'

import Table from '../components/table/Table'

import statusCards from '../assets/JsonData/status-card-data.json'

const API = process.env.REACT_APP_API;

const chartOptions = {
    series: [{
        name: 'Russia',
        data: [10, 18, 37, 54, 97, 71, 95, 123, 48]
    }, {
        name: 'China',
        data: [12, 53, 52, 40, 48, 48, 56, 58, 21]
    }, {
        name: 'Iran',
        data: [4, 4, 8, 13, 31, 39, 34, 27, 7]
    }, {
        name: 'North Korea',
        data: [4, 3, 4, 12, 25, 39, 24, 30, 8]
    },
    ],
    options: {
        color: ['#6ab04c', '#2980b9'],
        chart: {
            background: 'transparent'
        },
        dataLabels: {
            enabled: false
        }, 
        stroke: {
            curve: 'smooth'
        },
        xaxis: {
            categories: ['2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
        },
        legend: {
            position: 'top'
        },
        grid: {
            show: false
        }
    }
}

const TopThreatsHead = [
    'country',
    'country_code',
    'total_incidents'
]

var TopThreatsBody = [
    {
        "_id": "6138a0894ee0156be0553f69",
        "country": "Russia",
        "country_code": "RUS",
        "incidents_sent": 557,
        "latitude": "60.0000",
        "longitude": "100.0000"
    },
    {
        "_id": "6138a0894ee0156be0553f6e",
        "country": "China",
        "country_code": "CHN",
        "incidents_sent": 425,
        "latitude": "35.0000",
        "longitude": "105.0000"
    },
    {
        "_id": "6138a0894ee0156be0553f6a",
        "country": "Iran",
        "country_code": "IRN",
        "incidents_sent": 171,
        "latitude": "32.0000",
        "longitude": "53.0000"
    },
    {
        "_id": "6138a0894ee0156be0553f72",
        "country": "North Korea",
        "country_code": "PRK",
        "incidents_sent": 151,
        "latitude": "37.0000",
        "longitude": "127.5000"
    }
]

const getTopThreats = async () => {
    const doc_list = await fetch(`${API}/rawdata/topthreats`, {
        method: 'GET',
    })
    const doc_list_data = await doc_list.json();
    TopThreatsBody = doc_list_data
}

getTopThreats()

const renderCustomerHead = (item, index) => (
    <th key={index}>{item}</th>
)

const renderCustomerBody = (item, index) => (
    <tr key={index}>
        <td>{item.country}</td>
        <td>{item.country_code}</td>
        <td>{item.incidents_sent}</td>
    </tr>
)

const latestOrders = {
    head: [
        'year',
        'month',
        'group',
        'country',
        'reference'
    ],
    body: [
        {
            year: "2021",
            month: "May",
            group: "APT29",
            country: "Russia",
            url: "https://apt.thaicert.or.th/cgi-bin/showcard.cgi?g=APT%2029%2C%20Cozy%20Bear%2C%20The%20Dukes&n=1"
        },
        {
            year: "2021",
            month: "May",
            group: "Indrik",
            country: "Russia",
            url: "https://apt.thaicert.or.th/cgi-bin/showcard.cgi?g=Indrik%20Spider&n=1"
        },
        {
            year: "2021",
            month: "May",
            group: "Pinchy Spider",
            country: "Russia",
            url: "https://apt.thaicert.or.th/cgi-bin/showcard.cgi?g=Pinchy%20Spider%2C%20Gold%20Southfield&n=1"
        },
    ]
}

const renderOrderHead = (item, index) => (
    <th key={index}>{item}</th>
)

const renderOrderBody = (item, index) => (
    <tr key={index}>
        <td>{item.year}</td>
        <td>{item.month}</td>
        <td>{item.group}</td>
        <td>{item.country}</td>
        <td>
            <a href={item.url}>{item.url}</a>    
        </td>
    </tr>
)

const Dashboard = () => {

    


    return (
        <div>
            <h2 className='page-header'>DashBoard</h2>
            <div className="row">
                <div className="col-6">
                    <div className="row">
                        {
                            statusCards.map((item, index) => (
                                <div className="col-6">
                                    <StatusCard
                                        icon={item.icon}
                                        count={item.count}
                                        title={item.title}
                                    />
                                </div>
                            ))
                        }
                    </div>
                </div>
                <div className="col-6">
                    <div className="card full-height">
                        <Chart
                            options={chartOptions.options}
                            series={chartOptions.series}
                            type='line'
                            height='100%'

                        />
                    </div>
                </div>
                <div className="col-4">
                    <div className="card">
                        <div className="card__header">
                            <h3>Top Threats</h3>
                        </div>
                        <div className="card__body">
                            <Table
                                headData={TopThreatsHead}
                                renderHead = {(item, index) => renderCustomerHead(item, index)}
                                bodyData={TopThreatsBody}
                                renderBody = {(item, index) => renderCustomerBody(item, index)}
                            />
                        </div>
                        <div className="card__footer">
                            <Link to='/'>view all</Link>
                        </div>
                    </div>
                </div>
                <div className="col-8">
                    <div className="card full-height">
                        <div className="card__header">
                            <h3>Latest Incidents</h3>
                        </div>
                        <div className="card__body">
                            <Table
                                headData={latestOrders.head}
                                renderHead = {(item, index) => renderOrderHead(item, index)}
                                bodyData={latestOrders.body}
                                renderBody = {(item, index) => renderOrderBody(item, index)}
                            />
                        </div>
                        <div className="card__footer">
                            <Link to='/'>view all</Link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Dashboard

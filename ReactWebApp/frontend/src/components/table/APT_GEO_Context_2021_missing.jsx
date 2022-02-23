import React from 'react'

import './table.css'

const Table = props => {

    const APT_GEO_Context_2021_missing = [
        '',
        'country1',
        'country2',
        'incident_year',
        'country1_sent',
        'contry2_received',
        'Mutual',
        'incidents_0',
        'incidents_1',
        'incidents_2',
        'incidents_3',
        'incidents_4',
        'incidents_5',
    ]

    const renderHead = (item, index) => <th key={index}>{item}</th>

    const renderBody = (item, index) => (
        <tr key={index}>
            <td>{item.id}</td>
            <td>{item.country1_code}</td>
            <td>{item.country2_code}</td>
            <td>{item.incident_year}</td>
            <td>{item.country1_snt_incidents}</td>
            <td>{item.contry2_rvd_incidents}</td>
            <td>{item.country1_to_country2_incidents}</td>
            <td>{item.incidents_0}</td>
            <td>{item.incidents_1}</td>
            <td>{item.incidents_2}</td>
            <td>{item.incidents_3}</td>
            <td>{item.incidents_4}</td>
            <td>{item.incidents_5}</td>
        </tr>
    )

    return (
        <div>
          <div className="table-warpper">
            <table>
                {
                    props.renderHead ? (
                        <thead>
                            <tr>
                                {
                                    APT_GEO_Context_2021_missing.map((item, index) => renderHead(item, index))
                                }
                            </tr>
                        </thead>
                    ) : null
                }
                {
                    props.bodyData && props.renderBody ? (
                        <tbody>
                            {
                                props.bodyData.map((item, index) => renderBody(item, index))
                            }
                        </tbody>
                    ) : null
                }
            </table>
          </div> 
        </div>
    )
}

export default Table

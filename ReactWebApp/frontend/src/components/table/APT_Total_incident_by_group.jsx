import React from 'react'

import './table.css'

const Table = props => {

    const APT_Total_incident_by_group = [
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

    return (
        <div>
          <div className="table-warpper">
            <table>
                {
                    props.renderHead ? (
                        <thead>
                            <tr>
                                {
                                    APT_Total_incident_by_group.map((item, index) => renderHead(item, index))
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

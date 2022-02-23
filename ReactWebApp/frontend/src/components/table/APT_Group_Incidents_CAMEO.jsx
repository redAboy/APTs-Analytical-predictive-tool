import React from 'react'

import './table.css'

const Table = props => {

    const APT_Group_Incidents_CAMEO = [
        '',
        'group_name',
        'group_country',
        'cameo_country',
        'op_date',
        'op_month',
        'op_year',
    ]

    const renderHead = (item, index) => <th key={index}>{item}</th>

    const renderBody = (item, index) => (
        <tr key={index}>
            <td>{item.id}</td>
            <td>{item.group_name}</td>
            <td>{item.group_country}</td>
            <td>{item.cameo_country}</td>
            <td>{item.operation_date}</td>
            <td>{item.operation_month}</td>
            <td>{item.operation_year}</td>
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
                                    APT_Group_Incidents_CAMEO.map((item, index) => renderHead(item, index))
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

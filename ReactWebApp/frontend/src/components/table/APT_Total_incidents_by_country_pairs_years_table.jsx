import React from 'react'

import './table.css'

const Table = props => {

    const APT_Total_incident_by_country_pairs_years_table = [
        '',
        'year',
        'aggressor_country',
        'affected_country',
        'incidents',
    ]

    const renderHead = (item, index) => <th key={index}>{item}</th>

    const renderBody = (item, index) => (
        <tr key={index}>
            <td>{item.id}</td>
            <td>{item.year}</td>
            <td>{item.country1}</td>
            <td>{item.country2}</td>
            <td>{item.incidents}</td>
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
                                    APT_Total_incident_by_country_pairs_years_table.map((item, index) => renderHead(item, index))
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

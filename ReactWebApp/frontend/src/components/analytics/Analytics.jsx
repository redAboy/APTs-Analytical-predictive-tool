import React, {useState} from 'react'

import * as Tables from "../table"

const API = process.env.REACT_APP_API;

const Analytic = (props) => {

    const [formArray, setFormValue] = useState({})

    let query = `${API}/analysis/`

    const [bodyData, setBodyData] = useState()

    let renderBody = (item, index) => (
        <tr key={index}>
            <td>{item.id}</td>
            <td>{item.group_name}</td>
            <td>{item.country}</td>
            <td>{item.country_code}</td>
            <td>{item.incidents_sent}</td>
        </tr>
    )

    let Table = Tables[props.collection]

    const AddInput = (e, headers, formArray) => {
        setFormValue(formArray => ({
            ...formArray,
            [headers]: e
        }))
        console.log(formArray)
    }

    const queryCollection = async () => {

        query = query+"collection="+props.collection+"&"

        let counter = Object.keys(formArray).length

        for (var key in formArray){
            counter = counter - 1
            if (counter === 0){
                query = query+key+"="+formArray[key]
            }else {
                query = query+key+"="+formArray[key]+"&"
            }
        }

        const doc_list = await fetch(query, {
            method: 'GET',
        })
        const doc_list_data = await doc_list.json();

        setBodyData(doc_list_data)

        console.log(Table)
        setFormValue({})

    }

    return (
        <React.Fragment>
            <div className="row">
                {
                    props.headers ? (
                        <div className="col-6">
                            <div className="card">
                                <div className="card__body">
                                    {
                                        props.headers.map((headers, i) => 
                                            <div className="row form_container" key={i}>
                                                <div className="col-5 form_header_container">
                                                    <p className="form_header">{headers}</p>
                                                </div>
                                                <div className="col-7 form_input">
                                                    <input className="form" type="text" id={headers} onChange={(e) => AddInput(e.target.value, headers, formArray)}/>
                                                </div>
                                            </div>
                                        )
                                    }
                                </div>    
                            </div>
                        </div>
                    ): null
                }
                <div className="col-6">
                    
                </div>
                <div className="col-1">
                    <div className="card card_button">
                        <div className="card__body">
                            <button className="card_button_text" onClick={() => {queryCollection(); console.log(query)}}>Query</button>
                        </div>
                    </div>
                </div>
                {
                    bodyData ? (
                        <div className="col-12">
                            <div className="card">
                                <div className="card__body">
        
                                    <Table
                                        renderBody={renderBody}
                                        bodyData={bodyData}
                                    />
                                
                                </div>
                            </div>
                        </div>
                    ) : null
                }
                
            </div>
        </React.Fragment>
    )
}

export default Analytic

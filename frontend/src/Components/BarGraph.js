import * as React from 'react';
import { BarChart } from '@mui/x-charts/BarChart';
import { InputLabel, MenuItem, FormControl, Select } from '@mui/material'

import { useState, useEffect } from 'react';
import axios from 'axios';

const BarGraph = () => {
    const options = [
        { label: 'Operating System', value: 'operating_system' },
        { label: 'User Agent', value: 'user_agent' },
        { label: 'Request Type', value: 'request_type' },
        { label: 'API Endpoint', value: 'api_endpoint' }
    ]

    const [axisData, setAxisData] = useState([]);
    const [graphData, setGraphData] = useState([])
    const [fetchedData, setFetchedData] = useState(null)
    const [selectedOption, setSelectedOption] = useState(options[0])

    useEffect(() => {
        const backend_url = process.env.REACT_APP_BACKEND_URL
        const getData = async () => {
            const response = await axios.get(`${backend_url}dashboard/bargraph/`)
            setFetchedData(response.data)
        }

        getData()
    }, [])

    useEffect(() => {
        if (fetchedData) {
            const data = fetchedData[selectedOption.value]
            const xaxis = data.map((item) => {
                return item[selectedOption.value]
            })
            const values = data.map((item) => {
                return item.count
            })

            setAxisData(xaxis)
            setGraphData(values)
        }

    }, [selectedOption, fetchedData])


    const handleChange = (e) => {
        let value = e.target.value;
        if (value === "") value = "operating_system"
        const option = options.find((item) => item.value === value)
        setSelectedOption(option)
    }

    return (
        <>
            <FormControl sx={{ m: 1, minWidth: 150 }}>
                <InputLabel id="demo-simple-select-autowidth-label">Select Option</InputLabel>
                <Select
                    labelId="demo-simple-select-autowidth-label"
                    id="demo-simple-select-autowidth"

                    value={selectedOption.value}
                    onChange={handleChange}
                    autoWidth
                    label="Select Option"
                >
                    {/* <MenuItem value="">
                        <em>None</em>
                    </MenuItem> */}
                    {options.map((option) => {
                        return (
                            <MenuItem key={option.value} value={option.value}>{option.label}</MenuItem>
                        )
                    })}
                </Select>
            </FormControl>
            <BarChart
                xAxis={[{ scaleType: 'band', data: axisData }]}
                series={[{ data: graphData }]}
                width={800}
                height={500}
            />
        </>

    );
}

export default BarGraph

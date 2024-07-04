import { DataGrid } from '@mui/x-data-grid';

import axios from 'axios';
import { useState, useEffect } from 'react'
import { format } from 'date-fns'
import Typography from '@mui/material/Typography';
import DatePicker from './DatePicker'
import { Box } from '@mui/material'

const RequestTable = () => {

    const [startDate, setStartDate] = useState(null)
    const [endDate, setEndDate] = useState(null)

    const formatDate = (dateString) => {
        const date = new Date(dateString);
        return format(date, "yyyy-MM-dd hh:mm a");
    };


    const columns = [
        { field: 'id', headerName: 'ID', flex: 1 },
        { field: 'request_type', headerName: 'Request Type', flex: 1 },
        {
            field: 'request_time', headerName: 'Request Time', flex: 1,
            valueGetter: (params) => {
                // console.log(params)
                return formatDate(params)
            },
        },
        { field: 'api_endpoint', headerName: 'API Endpoint', flex: 1 },
        { field: 'payload', headerName: 'Payload', flex: 1 },
        { field: 'user_agent', headerName: 'User Agent', flex: 1 },
        { field: 'operating_system', headerName: 'Operating System', flex: 1 },
        { field: 'ip_address', headerName: 'IP Address', flex: 1 },
    ];
    const [requestData, setRequestData] = useState([])

    useEffect(() => {
        const getData = async () => {
            const backend_url = process.env.REACT_APP_BACKEND_URL
            const response = await axios.get(`${backend_url}dashboard/request_table/?start_date=${startDate}&end_date=${endDate}`)
            setRequestData(response.data)
        }

        getData();
    }, [startDate, endDate])

    const handleChangeStartDate = (date) => {
        if (date) {
            console.log(date.format('YYYY-MM-DD'))
            setStartDate(date.format('YYYY-MM-DD'))
        }
    }

    const handleChangeEndDate = (date) => {
        if (date) {
            // console.log(date.format('YYYY-MM-DD'))
            setEndDate(date.format('YYYY-MM-DD'))
        }
    }


    return (
        <div style={{ width: '100%' }}>
            <Typography variant='h4' sx={{ mb: 2 }}>
                Requests List
            </Typography>
            <Box
                sx={{ display: 'flex', justifyContent: 'flex-end', m: 2 }}
            >
                <Box sx={{ m: 1 }}>
                    <DatePicker label="Start Date" onChange={handleChangeStartDate} />
                </Box>
                <Box sx={{ m: 1 }}>
                    <DatePicker label="End Date" onChange={handleChangeEndDate} />
                </Box>

            </Box>

            <DataGrid
                rows={requestData}
                columns={columns}
                initialState={{
                    pagination: {
                        paginationModel: { page: 0, pageSize: 5 },
                    },
                }}
                pageSizeOptions={[5, 10, 15, 20]}
                columnBufferPx={0}
            />
        </div>
    );
}

export default RequestTable


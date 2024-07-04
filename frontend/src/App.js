import * as React from 'react';
import { styled } from '@mui/material/styles';
import Grid from '@mui/material/Grid';
import Paper from '@mui/material/Paper';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';

import BarGraph from './Components/BarGraph';
import Piechart from './Components/PieChart';
import RequestTable from './Components/RequestTable';

const Item = styled(Paper)(({ theme }) => ({
    backgroundColor: theme.palette.mode === 'dark' ? '#1A2027' : '#fff',
    ...theme.typography.body2,
    padding: theme.spacing(1),
    textAlign: 'center',
    color: theme.palette.text.secondary,
}));

const App = () => {
    return (
        <Box sx={{ width: '100%' }}>
            <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
                <Typography variant="h3" sx={{ ml: 4, mt: 4 }}>
                    Dashboard
                </Typography>
            </Box>
            <Grid container rowSpacing={1} columnSpacing={{ xs: 1, sm: 2, md: 3 }}>
                <Grid item xs={5}>
                    <Box
                        display="flex"
                        alignItems="center"
                        justifyContent="center"
                        height="100%"
                    >
                        <Item sx={{ m: 4, p: 4 }}>
                            <Piechart />
                        </Item>
                    </Box>


                </Grid>
                <Grid item xs={7}>
                    <Box
                        display="flex"
                        alignItems="flex"
                        justifyContent="center"
                        height="100%"
                    >
                        <Item sx={{ m: 4, p: 4 }}>
                            <BarGraph />
                        </Item>
                    </Box>


                </Grid>
                <Grid item xs={12}>
                    <Item sx={{ m: 4, p: 4 }}>
                        <RequestTable />
                    </Item>
                </Grid>

            </Grid>
        </Box>
    );
}

export default App;



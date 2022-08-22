import * as React from 'react';
import {useState} from 'react';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Box from '@mui/material/Box';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import {createTheme, ThemeProvider} from '@mui/material/styles';
import PropTypes from 'prop-types';
import {Alert, Stack} from "@mui/material";
import {loginUser} from "../services/api";

const theme = createTheme();


export default function Login({ setToken }) {
    const [email, setEmail] = useState();
    const [password, setPassword] = useState();
    const [errorMessage, setErrorMessage] = useState({
        email: '',
        password: '',
    });

    const handleSubmit = async event => {
        event.preventDefault();
        const response = await loginUser({
            email,
            password
        });
        if (response.errors) {
            setErrorMessage(response.errors);
        }
        setToken(response);
    };

    return (
        <ThemeProvider theme={theme}>
            <Container component="main" maxWidth="xs">
                <CssBaseline />
                <Box
                    sx={{
                        marginTop: 8,
                        display: 'flex',
                        flexDirection: 'column',
                        alignItems: 'center',
                    }}
                >
                    <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
                        <LockOutlinedIcon />
                    </Avatar>
                    <Typography component="h1" variant="h5">
                        Sign in
                    </Typography>
                    <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
                        <TextField
                            margin="normal"
                            required
                            fullWidth
                            id="email"
                            label="Email Address"
                            name="email"
                            autoComplete="email"
                            autoFocus
                            onChange={event => setEmail(event.target.value)}
                            error={!!errorMessage?.email}
                            helperText={errorMessage?.email ? errorMessage.email[0] : null}
                        />
                        <TextField
                            margin="normal"
                            required
                            fullWidth
                            name="password"
                            label="Password"
                            type="password"
                            id="password"
                            autoComplete="current-password"
                            onChange={event => setPassword(event.target.value)}
                            error={!!errorMessage?.password}
                            helperText={errorMessage?.password ? errorMessage.password[0] : null}
                        />
                        <FormControlLabel
                            control={<Checkbox value="remember" color="primary" />}
                            label="Remember me"
                        />
                        <Button
                            type="submit"
                            fullWidth
                            variant="contained"
                            sx={{ mt: 3, mb: 2 }}
                        >
                            Sign In
                        </Button>
                        {errorMessage &&  errorMessage[0] &&
                            <Stack sx={{ width: '100%' }} spacing={2}>
                                <Alert severity="error">{errorMessage[0]}</Alert>
                            </Stack>
                        }
                    </Box>
                </Box>
            </Container>
        </ThemeProvider>
    );

    Login.propTypes = {
        setToken: PropTypes.func.isRequired
    }
}
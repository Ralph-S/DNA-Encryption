import { useState, useEffect } from 'react';
import { Container, Box, List, ListItem, ListItemText, Paper, Typography, Grid, TextField, Button, Card, CardContent } from '@mui/material';
import VpnKeyIcon from '@mui/icons-material/VpnKey';
import axios from 'axios';

function Secrets() {
  const [originalSecrets, setOriginalSecrets] = useState([]);
  const [encryptedSecrets, setEncryptedSecrets] = useState([]);
  const [newSecret, setNewSecret] = useState('');
  const [key, setKey] = useState('');

  useEffect(() => {
    // Dummy data for original secrets
    const dummyOriginalSecrets = ['Hello World! This is a test of our Application, Hope you enjoy!'];
    setOriginalSecrets(dummyOriginalSecrets);

    // Dummy data for encrypted secrets
    const dummyEncryptedSecrets = [
      'CTCTTTAACCGTTCGTGATGGTCACAACGGTAATTTATTATTTGAAGCAGGTGGCGAGAGCCAC',
    ];
    setEncryptedSecrets(dummyEncryptedSecrets);
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();

    // Validate key length
    const formattedKey = key.replace(/\s/g, ''); // Remove spaces
    if (formattedKey.length !== 32) {
      alert('Please provide a key that is exactly 32 characters long (and spaces in between each 2 characters).');
      return;
    }

    axios.post('http://localhost:5000/process-data', { plaintext: newSecret, key: key })
      .then(response => {
        if (response.status === 200) {
          setOriginalSecrets([...originalSecrets, newSecret]);
          setEncryptedSecrets([...encryptedSecrets, response.data]);
        } else {
          console.error('Failed to post secret');
        }
      })
      .catch(error => {
        console.error('Error posting secret:', error);
      });

    setNewSecret('');
    setKey('');
  };

  return (
    <Container maxWidth="md">
      <Box sx={{ mb: 4, display: 'flex', flexDirection: 'column', alignItems: 'center', marginTop: "4.8rem" }}>
        <VpnKeyIcon sx={{ fontSize: 80 }} />
        <Typography variant="h3" gutterBottom component="div">
          Secrets
        </Typography>
        <Typography variant="body1">
          Share your secrets safely!
        </Typography>
      </Box>

      <Box sx={{ marginBottom: "2rem" }} mt={4}>
        <Card>
          <CardContent>
            <Typography variant="h6" gutterBottom>
              Post a New Secret
            </Typography>
            <form onSubmit={handleSubmit}>
              <TextField
                label="Key (e.g: AB CD 12 34 56 EF GH 78 AB CD 12 34 56 EF GH 78)"
                variant="outlined"
                fullWidth
                value={key}
                onChange={(e) => setKey(e.target.value)}
                sx={{ mt: 1, marginBottom:"1rem" }}
              />
              <TextField
                label="Your secret here"
                variant="outlined"
                fullWidth
                multiline
                rows={4} // Adjust the number of rows as needed
                value={newSecret}
                onChange={(e) => setNewSecret(e.target.value)}
                sx={{ mt: 1, marginBottom:"0.5rem" }}
              />
              <Button
                variant="contained"
                type="submit"
                sx={{
                  mt: 1,
                  marginBottom: "0.2rem",
                  backgroundColor: "black",
                  "&:hover": {
                    backgroundColor: "#4C4C4C",
                  },
                }}
              >
                Submit
              </Button>
            </form>
          </CardContent>
        </Card>
      </Box>

      <Grid container spacing={4} sx={{ mt: 1, marginBottom:"5rem" }}>
        <Grid item xs={12} md={6}>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>
                Original Secrets
              </Typography>
              <List dense={true}>
                {originalSecrets.map((secret, index) => (
                  <ListItem key={index} sx={{ paddingY: 1 }}>
                    <ListItemText primary={secret} />
                  </ListItem>
                ))}
              </List>
            </CardContent>
          </Card>
        </Grid>

        <Grid item xs={12} md={6}>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>
                Encrypted Secrets
              </Typography>
              <List dense={true} sx={{ maxHeight: '200px', overflow: 'auto' }}> {/* Adjust the maxHeight as needed */}
                {encryptedSecrets.map((secret, index) => (
                  <ListItem key={index} sx={{ paddingY: 1 }}>
                    <ListItemText primary={secret} />
                  </ListItem>
                ))}
              </List>
            </CardContent>
          </Card>
        </Grid>
      </Grid>
    </Container>
  );
}

export default Secrets;

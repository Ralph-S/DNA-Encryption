import { useState, useEffect } from 'react';
import { Container, Box, List, ListItem, ListItemText, Paper, Typography, Grid, TextField, Button, Card, CardContent } from '@mui/material';
import VpnKeyIcon from '@mui/icons-material/VpnKey';
import axios from 'axios';

function Secrets() {
  const [originalSecrets, setOriginalSecrets] = useState([]);
  const [encryptedSecrets, setEncryptedSecrets] = useState([]);
  const [newSecret, setNewSecret] = useState('');

  useEffect(() => {
    // Dummy data for original secrets
    const dummyOriginalSecrets = ['Original Secret 1', 'Original Secret 2', 'Original Secret 3'];
    setOriginalSecrets(dummyOriginalSecrets);

    // Dummy data for encrypted secrets
    const dummyEncryptedSecrets = ['Encrypted Secret 1', 'Encrypted Secret 2', 'Encrypted Secret 3'];
    setEncryptedSecrets(dummyEncryptedSecrets);
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('http://localhost:5000/post-plaintext', { plaintext: newSecret })
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
  };


  return (
    <Container maxWidth="sm">
      <Box sx={{ mb: 4, display: 'flex', flexDirection: 'column', alignItems: 'center', marginTop: "4.8rem" }}>
        <VpnKeyIcon sx={{ fontSize: 80 }} />
        <Typography variant="h3" gutterBottom component="div">
          Secrets
        </Typography>
        <Typography variant="body1">
          Share your secrets safely!
        </Typography>
      </Box>

      <Grid container spacing={4}> {/* Grid container for secret sections */}
        <Grid item xs={12} md={6}> {/* Left section for original secrets */}
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

        <Grid item xs={12} md={6}> {/* Right section for encrypted secrets */}
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>
                Encrypted Secrets
              </Typography>
              <List dense={true}>
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

      <Box sx={{ marginBottom: "2rem" }} mt={4}> {/* Section for posting new secret */}
        <Card>
          <CardContent>
            <Typography variant="h6" gutterBottom>
              Post a New Secret
            </Typography>
            <form onSubmit={handleSubmit}>
              <TextField
                label="Your secret here"
                variant="outlined"
                fullWidth
                value={newSecret}
                onChange={(e) => setNewSecret(e.target.value)}
              />
              <Button variant="contained" type="submit" sx={{ mt: 2 }}>
                Submit
              </Button>
            </form>
          </CardContent>
        </Card>
      </Box>
    </Container>
  );
}

export default Secrets;

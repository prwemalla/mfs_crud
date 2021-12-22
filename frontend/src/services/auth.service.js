import axios from 'axios';

const API_URL = 'http://localhost:8080/auth/';

class AuthService {
  login(user) {
    return axios
      .post(API_URL + 'login', {
        email: user.username,
        password: user.password
      })
      .then(response => {
        if (response.data.token) {
          var jwt_token = response.data.token
          var base64_jwt_token = jwt_token.split('.')[1];
          var base64_data = base64_jwt_token.replace(/-/g, '+').replace(/_/g, '/');
          var jsonPayload = decodeURIComponent(atob(base64_data).split('').map(function(c) {
              return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
          }).join(''));
          var auth_user = JSON.parse(jsonPayload);
          auth_user.accessToken = jwt_token;
          localStorage.setItem('auth_user', JSON.stringify(auth_user));
          return auth_user;
        }
      })
      .then(auth_user => {
        return axios.get(API_URL + 'user', { headers: { Authorization: 'Bearer ' + auth_user.accessToken } })
      })
      .then(response => {
        var auth_user = JSON.parse(localStorage.getItem('auth_user'));
        auth_user.user_details = response.data
        localStorage.setItem('user', JSON.stringify(auth_user));
        return auth_user
      });
  }

  logout() {
    localStorage.removeItem('user');
  }

  register(user) {
    return axios.post(API_URL + 'signup', {
      username: user.username,
      email: user.email,
      password: user.password
    });
  }
}

export default new AuthService();

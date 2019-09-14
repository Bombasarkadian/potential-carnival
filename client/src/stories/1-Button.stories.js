import React from 'react';
import { action } from '@storybook/addon-actions';
import Button from '@material-ui/core/Button';

export default {
  title: 'Button'
};

export const text = () => (
  <Button variant="contained" color="primary" onClick={action('clicked')}>
    Hello Button
  </Button>
);

export const emoji = () => (
  <Button variant="contained" color="primary" onClick={action('clicked')}>
    <span role="img" aria-label="so cool">
      😀 😎 👍 💯
    </span>
  </Button>
);

import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import PropTypes from 'prop-types';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';

import { PureProgress } from './Progress';

const useStyles = makeStyles({
  appBar: {
    top: 'auto',
    bottom: 0
  },
  appBarPadder: {
    height: 64
  }
});

function BottomAppBar({ content }) {
  const classes = useStyles();

  return (
    <div>
      <div className={classes.appBarPadder}></div>
      <AppBar position="fixed" color="primary" className={classes.appBar}>
        <Toolbar>{content}</Toolbar>
      </AppBar>
    </div>
  );
}

BottomAppBar.propTypes = {
  content: PropTypes.element.isRequired
};

BottomAppBar.defaultProps = {
  content: <PureProgress progress={{ count: 3, max: 10 }} />
};

export default BottomAppBar;

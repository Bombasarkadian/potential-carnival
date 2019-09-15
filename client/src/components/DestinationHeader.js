import React, { Component } from 'react';
import { withStyles } from '@material-ui/styles';
import Typography from '@material-ui/core/Typography';
import { connect } from 'react-redux';
import compose from 'recompose/compose';
import Card from '@material-ui/core/Card';
import Grid from '@material-ui/core/Grid';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Button from '@material-ui/core/Button';
import DestinationDetails from './DestinationDetails';
import ShoppingCartTwoToneIcon from '@material-ui/icons/ShoppingCartTwoTone';
import RefreshTwoToneIcon from '@material-ui/icons/RefreshTwoTone';

import Map from './Map';
import store from './../data';
import { fetchDecision } from '../data/decision/actions';
import FullLoader from './FullLoader';

const styles = {
  card: {
    maxWidth: 1051,
    margin: 20,
    backgroundColor: '#fefcf5'
  },
  media: {
    height: 287
  },
  cardActions: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'space-between'
  }
};

class PureDestinationHeader extends Component {
  componentDidUpdate(prevProps, prevState, snapshot) {
    if (
      !this.props.decision &&
      !this.props.isImageSaving &&
      !this.props.isDecisionFetching
    ) {
      store.dispatch(fetchDecision(this.props.sessionID));
    }
  }

  render() {
    const { classes } = this.props;

    if (!this.props.decision) return <FullLoader />;

    console.log(this.props.decision);

    return (
      <Card className={classes.card} raised={true}>
        <CardMedia
          className={classes.media}
          image={this.props.decision.img}
          title={this.props.decision.name}
        />
        <CardContent>
          <Typography gutterBottom variant="h5" component="h2">
            {this.props.decision.country} - {this.props.decision.name}
          </Typography>
          <Grid container>
            <Grid item md={7}>
              <Typography variant="body2" color="textSecondary" component="p">
                {this.props.decision.description}
              </Typography>
              <DestinationDetails decision={this.props.decision} />
            </Grid>
            <Grid item md={5}>
              <div style={{ position: 'relative' }}>
                <div
                  style={{
                    width: 300,
                    height: 300,
                    borderRadius: '50%',
                    background:
                      'background-image: radial-gradient(circle, rgba(169, 206, 233, 0) 0%, rgba(146, 207, 255, 0) 60%, rgba(52, 119, 190, 0.4) 85%)',
                    position: 'absolute',
                    zIndex: '999',
                    top: 0,
                    bottom: 0,
                    left: 0,
                    right: 0
                  }}
                ></div>
                <Map
                  latitude={this.props.decision.lat}
                  longitude={this.props.decision.long}
                />
              </div>
            </Grid>
          </Grid>
        </CardContent>
        <CardActions className={classes.cardActions}>
          <Button color="primary" href="/">
            Find something else
            <RefreshTwoToneIcon style={{ marginLeft: 10 }} />
          </Button>
          <Button
            style={{ paddingLeft: 20 }}
            color="secondary"
            variant="contained"
            href={this.props.decision.price.url}
          >
            {this.props.decision.price.price
              ? `Book this flight for ${this.props.decision.price.price} ${this.props.decision.price.currency}`
              : 'Find this flight on Lot.com'}
            <ShoppingCartTwoToneIcon style={{ marginLeft: 10 }} />
          </Button>
        </CardActions>
      </Card>
    );
  }
}

export default compose(
  withStyles(styles),
  connect(({ session, decision, images }) => {
    return {
      sessionID: session.sessionID,
      decision: decision.decision,
      isDecisionFetching: decision.isDecisionFetching,
      isImageSaving: images.isImageSaving
    };
  })
)(PureDestinationHeader);

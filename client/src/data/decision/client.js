import { BaseClient } from '../client';

const fetch = require('node-fetch');

export class DecisionClient extends BaseClient {
  _getHeaders = sessionID => {
    return {
      'SESSION-ID': sessionID,
      'Content-Type': 'application/json'
    };
  };

  fetchDecision = async sessionID => {
    let decision = await fetch(this._url() + 'decisions/', {
      method: 'GET',
      headers: this._getHeaders(sessionID),
      mode: 'cors'
    });

    return await decision.json();
  };
}

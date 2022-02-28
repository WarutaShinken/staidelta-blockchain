const staidelta = require('../../util/staidelta');

describe('staidelta', () => {
  it('converts number mojo to staidelta', () => {
    const result = staidelta.mojo_to_staidelta(1000000);

    expect(result).toBe(0.000001);
  });
  it('converts string mojo to staidelta', () => {
    const result = staidelta.mojo_to_staidelta('1000000');

    expect(result).toBe(0.000001);
  });
  it('converts number mojo to staidelta string', () => {
    const result = staidelta.mojo_to_staidelta_string(1000000);

    expect(result).toBe('0.000001');
  });
  it('converts string mojo to staidelta string', () => {
    const result = staidelta.mojo_to_staidelta_string('1000000');

    expect(result).toBe('0.000001');
  });
  it('converts number staidelta to mojo', () => {
    const result = staidelta.staidelta_to_mojo(0.000001);

    expect(result).toBe(1000000);
  });
  it('converts string staidelta to mojo', () => {
    const result = staidelta.staidelta_to_mojo('0.000001');

    expect(result).toBe(1000000);
  });
  it('converts number mojo to colouredcoin', () => {
    const result = staidelta.mojo_to_colouredcoin(1000000);

    expect(result).toBe(1000);
  });
  it('converts string mojo to colouredcoin', () => {
    const result = staidelta.mojo_to_colouredcoin('1000000');

    expect(result).toBe(1000);
  });
  it('converts number mojo to colouredcoin string', () => {
    const result = staidelta.mojo_to_colouredcoin_string(1000000);

    expect(result).toBe('1,000');
  });
  it('converts string mojo to colouredcoin string', () => {
    const result = staidelta.mojo_to_colouredcoin_string('1000000');

    expect(result).toBe('1,000');
  });
  it('converts number colouredcoin to mojo', () => {
    const result = staidelta.colouredcoin_to_mojo(1000);

    expect(result).toBe(1000000);
  });
  it('converts string colouredcoin to mojo', () => {
    const result = staidelta.colouredcoin_to_mojo('1000');

    expect(result).toBe(1000000);
  });
});

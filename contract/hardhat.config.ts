// @ts-ignore
import * as tdly from "@tenderly/hardhat-tenderly";
// @ts-ignore
import { HardhatUserConfig } from "hardhat/config";
import * as dotenv from "dotenv";

tdly.setup();

dotenv.config();

const { TENDERLY_PRIVATE_VERIFICATION } = process.env;

const priaveteVerification = TENDERLY_PRIVATE_VERIFICATION === "true";

console.log("Using private verification? ", priaveteVerification, TENDERLY_PRIVATE_VERIFICATION);

const config: HardhatUserConfig = {
  solidity: "0.8.9",

  networks: {
    tenderly: {
      chainId: 1,
      url: `https://rpc.tenderly.co/fork/4c7520f0-e583-4df2-aaa3-f416988477a8`,
    },
  },
  tenderly: {
    project: "deep-cookie",
    username: "Yield",
    forkNetwork: "4c7520f0-e583-4df2-aaa3-f416988477a8",
  },
};

// eslint-disable-next-line import/no-default-export
export default config;

import { ethers, tenderly } from "hardhat";

async function main() {
  const Contract = await ethers.getContractFactory("contracts/Contract.sol:Contract");
  const contract = await Contract.deploy();

  await contract.deployed();
  const address = contract.address;
  console.log(" {Contract} deployed to:", address);
  await tenderly.verify({
    address,
    name: "Contract",
  });

  const Test = await ethers.getContractFactory("Test");
  const test = await Test.deploy();

  await test.deployed();
  const testAddress = test.address;
  console.log(" {Test} deployed to:", testAddress);
  await tenderly.verify({
    address:testAddress,
    name: "contracts/Test.sol:Contract",
  });

  await tenderly.verify({
    address,
    name: "contracts/Contract.sol:Contract",
  });
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});

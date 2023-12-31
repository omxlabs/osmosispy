"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Minter(google.protobuf.message.Message):
    """Minter represents the minting state."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EPOCH_PROVISIONS_FIELD_NUMBER: builtins.int
    epoch_provisions: builtins.str
    """epoch_provisions represent rewards for the current epoch."""
    def __init__(
        self,
        *,
        epoch_provisions: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["epoch_provisions", b"epoch_provisions"]) -> None: ...

global___Minter = Minter

class WeightedAddress(google.protobuf.message.Message):
    """WeightedAddress represents an address with a weight assigned to it.
    The weight is used to determine the proportion of the total minted
    tokens to be minted to the address.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESS_FIELD_NUMBER: builtins.int
    WEIGHT_FIELD_NUMBER: builtins.int
    address: builtins.str
    weight: builtins.str
    def __init__(
        self,
        *,
        address: builtins.str = ...,
        weight: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["address", b"address", "weight", b"weight"]) -> None: ...

global___WeightedAddress = WeightedAddress

class DistributionProportions(google.protobuf.message.Message):
    """DistributionProportions defines the distribution proportions of the minted
    denom. In other words, defines which stakeholders will receive the minted
    denoms and how much.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STAKING_FIELD_NUMBER: builtins.int
    POOL_INCENTIVES_FIELD_NUMBER: builtins.int
    DEVELOPER_REWARDS_FIELD_NUMBER: builtins.int
    COMMUNITY_POOL_FIELD_NUMBER: builtins.int
    staking: builtins.str
    """staking defines the proportion of the minted mint_denom that is to be
    allocated as staking rewards.
    """
    pool_incentives: builtins.str
    """pool_incentives defines the proportion of the minted mint_denom that is
    to be allocated as pool incentives.
    """
    developer_rewards: builtins.str
    """developer_rewards defines the proportion of the minted mint_denom that is
    to be allocated to developer rewards address.
    """
    community_pool: builtins.str
    """community_pool defines the proportion of the minted mint_denom that is
    to be allocated to the community pool.
    """
    def __init__(
        self,
        *,
        staking: builtins.str = ...,
        pool_incentives: builtins.str = ...,
        developer_rewards: builtins.str = ...,
        community_pool: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["community_pool", b"community_pool", "developer_rewards", b"developer_rewards", "pool_incentives", b"pool_incentives", "staking", b"staking"]) -> None: ...

global___DistributionProportions = DistributionProportions

class Params(google.protobuf.message.Message):
    """Params holds parameters for the x/mint module."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MINT_DENOM_FIELD_NUMBER: builtins.int
    GENESIS_EPOCH_PROVISIONS_FIELD_NUMBER: builtins.int
    EPOCH_IDENTIFIER_FIELD_NUMBER: builtins.int
    REDUCTION_PERIOD_IN_EPOCHS_FIELD_NUMBER: builtins.int
    REDUCTION_FACTOR_FIELD_NUMBER: builtins.int
    DISTRIBUTION_PROPORTIONS_FIELD_NUMBER: builtins.int
    WEIGHTED_DEVELOPER_REWARDS_RECEIVERS_FIELD_NUMBER: builtins.int
    MINTING_REWARDS_DISTRIBUTION_START_EPOCH_FIELD_NUMBER: builtins.int
    mint_denom: builtins.str
    """mint_denom is the denom of the coin to mint."""
    genesis_epoch_provisions: builtins.str
    """genesis_epoch_provisions epoch provisions from the first epoch."""
    epoch_identifier: builtins.str
    """epoch_identifier mint epoch identifier e.g. (day, week)."""
    reduction_period_in_epochs: builtins.int
    """reduction_period_in_epochs the number of epochs it takes
    to reduce the rewards.
    """
    reduction_factor: builtins.str
    """reduction_factor is the reduction multiplier to execute
    at the end of each period set by reduction_period_in_epochs.
    """
    @property
    def distribution_proportions(self) -> global___DistributionProportions:
        """distribution_proportions defines the distribution proportions of the minted
        denom. In other words, defines which stakeholders will receive the minted
        denoms and how much.
        """
    @property
    def weighted_developer_rewards_receivers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___WeightedAddress]:
        """weighted_developer_rewards_receivers is the address to receive developer
        rewards with weights assignedt to each address. The final amount that each
        address receives is: epoch_provisions *
        distribution_proportions.developer_rewards * Address's Weight.
        """
    minting_rewards_distribution_start_epoch: builtins.int
    """minting_rewards_distribution_start_epoch start epoch to distribute minting
    rewards
    """
    def __init__(
        self,
        *,
        mint_denom: builtins.str = ...,
        genesis_epoch_provisions: builtins.str = ...,
        epoch_identifier: builtins.str = ...,
        reduction_period_in_epochs: builtins.int = ...,
        reduction_factor: builtins.str = ...,
        distribution_proportions: global___DistributionProportions | None = ...,
        weighted_developer_rewards_receivers: collections.abc.Iterable[global___WeightedAddress] | None = ...,
        minting_rewards_distribution_start_epoch: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["distribution_proportions", b"distribution_proportions"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["distribution_proportions", b"distribution_proportions", "epoch_identifier", b"epoch_identifier", "genesis_epoch_provisions", b"genesis_epoch_provisions", "mint_denom", b"mint_denom", "minting_rewards_distribution_start_epoch", b"minting_rewards_distribution_start_epoch", "reduction_factor", b"reduction_factor", "reduction_period_in_epochs", b"reduction_period_in_epochs", "weighted_developer_rewards_receivers", b"weighted_developer_rewards_receivers"]) -> None: ...

global___Params = Params

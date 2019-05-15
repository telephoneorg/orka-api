# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_str_schema 1'] = '''schema {
  query: Query
  mutation: Mutation
}

input AddFacilitatorContextInput {
  profile: ProfileInput
  npi: String!
  availability: String!
  licenses: [FacilitatorLicenseInput]
  clientMutationId: String
}

type AddFacilitatorContextPayload {
  ok: Boolean
  facilitatorContext: FacilitatorContext
  clientMutationId: String
}

input AddFacilitatorLicenseInput {
  facilitatorContextId: ID!
  facilitatorLicense: FacilitatorLicenseInput
  clientMutationId: String
}

type AddFacilitatorLicensePayload {
  ok: Boolean
  facilitatorLicense: FacilitatorLicense
  clientMutationId: String
}

input AddParticipantContextInput {
  profile: ProfileInput!
  clientMutationId: String
}

type AddParticipantContextPayload {
  ok: Boolean
  participantContext: ParticipantContext
  clientMutationId: String
}

input CreateMeInput {
  firstName: String!
  lastName: String!
  cellPhone: String
  dob: Date!
  notificationPolicy: NotificationPolicyInput!
  clientMutationId: String
}

type CreateMePayload {
  ok: Boolean
  user: User
  clientMutationId: String
}

scalar Date

scalar DateTime

input DeleteMeInput {
  clientMutationId: String
}

type DeleteMePayload {
  ok: Boolean
  userId: ID!
  clientMutationId: String
}

type FacilitatorContext implements Node, UserContext {
  created: DateTime
  updated: DateTime
  id: ID!
  type: UserContextType
  userId: Int!
  status: UserContextStatus
  npi: String
  availability: String
  licenses(before: String, after: String, first: Int, last: Int): FacilitatorLicenseConnection
  user: User
  profile: Profile
}

input FacilitatorContextInput {
  profile: ProfileInput
  npi: String
  availability: String
  licenses: [FacilitatorLicenseInput]
}

type FacilitatorLicense implements Node {
  created: DateTime!
  updated: DateTime!
  id: ID!
  facilitatorContextId: Int!
  type: LicenseType!
  number: String!
  expiry: String
  usState: UsState
  facilitatorContext: FacilitatorContext
}

type FacilitatorLicenseConnection {
  pageInfo: PageInfo!
  edges: [FacilitatorLicenseEdge]!
}

type FacilitatorLicenseEdge {
  node: FacilitatorLicense
  cursor: String!
}

input FacilitatorLicenseInput {
  type: LicenseType
  number: String
  expiry: Date
  usState: UsState
}

type Identity implements Node {
  created: DateTime!
  updated: DateTime!
  id: ID!
  userId: Int!
  provider: IdentityProvider!
  subject: String!
  user: User
}

type IdentityConnection {
  pageInfo: PageInfo!
  edges: [IdentityEdge]!
}

type IdentityEdge {
  node: Identity
  cursor: String!
}

enum IdentityProvider {
  CUP
}

enum LicenseType {
  TBD
}

type Mutation {
  createMe(input: CreateMeInput!): CreateMePayload
  updateMe(input: UpdateMeInput!): UpdateMePayload
  deleteMe(input: DeleteMeInput!): DeleteMePayload
  addParticipantContext(input: AddParticipantContextInput!): AddParticipantContextPayload
  updateParticipantContext(input: UpdateParticipantContextInput!): UpdateParticipantContextPayload
  removeParticipantContext(input: RemoveParticipantContextInput!): RemoveParticipantContextPayload
  addFacilitatorContext(input: AddFacilitatorContextInput!): AddFacilitatorContextPayload
  updateFacilitatorContext(input: UpdateFacilitatorContextInput!): UpdateFacilitatorContextPayload
  removeFacilitatorContext(input: RemoveFacilitatorContextInput!): RemoveFacilitatorContextPayload
  addFacilitatorLicense(input: AddFacilitatorLicenseInput!): AddFacilitatorLicensePayload
  removeFacilitatorLicense(input: RemoveFacilitatorLicenseInput!): RemoveFacilitatorLicensePayload
}

interface Node {
  id: ID!
}

type NotificationPolicy implements Node {
  created: DateTime!
  updated: DateTime!
  id: ID!
  userId: Int!
  allowEmail: Boolean
  allowSms: Boolean
  allowMarketing: Boolean
  user: User
}

input NotificationPolicyInput {
  allowEmail: Boolean
  allowSms: Boolean
  allowMarketing: Boolean
}

type PageInfo {
  hasNextPage: Boolean!
  hasPreviousPage: Boolean!
  startCursor: String
  endCursor: String
}

type ParticipantContext implements Node, UserContext {
  created: DateTime
  updated: DateTime
  id: ID!
  type: UserContextType
  userId: Int!
  status: UserContextStatus
  user: User
  profile: Profile
}

input ParticipantContextInput {
  profile: ProfileInput
}

type Profile implements Node {
  created: DateTime!
  updated: DateTime!
  id: ID!
  userContextId: Int!
  displayName: String
  avatar: String
  bio: String
}

input ProfileInput {
  displayName: String
  avatar: String
  bio: String
}

type Query {
  node(id: ID!): Node
  me: User!
  profile(id: ID!): Profile!
}

input RemoveFacilitatorContextInput {
  id: ID!
  clientMutationId: String
}

type RemoveFacilitatorContextPayload {
  ok: Boolean
  facilitatorContextId: ID!
  clientMutationId: String
}

input RemoveFacilitatorLicenseInput {
  facilitatorContextId: ID!
  facilitatorLicenseId: ID!
  clientMutationId: String
}

type RemoveFacilitatorLicensePayload {
  ok: Boolean
  facilitatorLicenseId: ID!
  clientMutationId: String
}

input RemoveParticipantContextInput {
  id: ID!
  clientMutationId: String
}

type RemoveParticipantContextPayload {
  ok: Boolean
  participantContextId: ID!
  clientMutationId: String
}

input UpdateFacilitatorContextInput {
  id: ID!
  facilitatorContext: FacilitatorContextInput
  clientMutationId: String
}

type UpdateFacilitatorContextPayload {
  ok: Boolean
  facilitatorContext: FacilitatorContext
  clientMutationId: String
}

input UpdateMeInput {
  firstName: String
  lastName: String
  cellPhone: String
  dob: Date
  notificationPolicy: NotificationPolicyInput
  clientMutationId: String
}

type UpdateMePayload {
  ok: Boolean
  user: User
  clientMutationId: String
}

input UpdateParticipantContextInput {
  id: ID!
  participantContext: ParticipantContextInput
  clientMutationId: String
}

type UpdateParticipantContextPayload {
  ok: Boolean
  participantContext: ParticipantContext
  clientMutationId: String
}

enum UsState {
  AL
  AK
  AS
  AZ
  AR
  CA
  CO
  CT
  DE
  DC
  FM
  FL
  GA
  GU
  HI
  ID
  IL
  IN
  IA
  KS
  KY
  LA
  ME
  MH
  MD
  MA
  MI
  MN
  MS
  MO
  MT
  NE
  NV
  NH
  NJ
  NM
  NY
  NC
  ND
  MP
  OH
  OK
  OR
  PW
  PA
  PR
  RI
  SC
  SD
  TN
  TX
  UT
  VT
  VI
  VA
  WA
  WV
  WI
  WY
}

type User implements Node {
  created: DateTime!
  updated: DateTime!
  id: ID!
  firstName: String!
  lastName: String!
  email: String!
  cellPhone: String
  dob: String
  identities(before: String, after: String, first: Int, last: Int): IdentityConnection
  contexts(before: String, after: String, first: Int, last: Int): UserContextConnection
  notificationPolicy: NotificationPolicy
}

interface UserContext {
  id: ID!
  type: UserContextType
  status: UserContextStatus
  profile: Profile
  created: DateTime
  updated: DateTime
}

type UserContextConnection {
  pageInfo: PageInfo!
  edges: [UserContextEdge]!
  count: Int
}

type UserContextEdge {
  node: UserContext
  cursor: String!
}

enum UserContextStatus {
  CREATED
  DELETED
  VERIFIED
}

enum UserContextType {
  BASE
  PARTICIPANT
  FACILITATOR
  EMPLOYEE
  COMPANY
}
'''
